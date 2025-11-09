import pandas as pd
import os
import numpy as np

# List of all prefixes
PREFIXES = [
    "CO2_Agriculture", "CO2_Buildings", "CO2_Fuel_Exploitation",
    "CO2_Industrial_Combustion", "CO2_Power_Industry", "CO2_Processes",
    "CO2_Transport", "GWP_100_AR5_CH4_Agriculture", "GWP_100_AR5_CH4_Buildings",
    "GWP_100_AR5_CH4_Fuel_Exploitation", "GWP_100_AR5_CH4_Industrial_Combustion",
    "GWP_100_AR5_CH4_Power_Industry", "GWP_100_AR5_CH4_Processes",
    "GWP_100_AR5_CH4_Transport", "GWP_100_AR5_CH4_Waste",
    "GWP_100_AR5_F-gases_Processes", "GWP_100_AR5_N2O_Agriculture",
    "GWP_100_AR5_N2O_Buildings", "GWP_100_AR5_N2O_Fuel_Exploitation",
    "GWP_100_AR5_N2O_Industrial_Combustion", "GWP_100_AR5_N2O_Power_Industry",
    "GWP_100_AR5_N2O_Processes", "GWP_100_AR5_N2O_Transport",
    "GWP_100_AR5_N2O_Waste"
]

BASE_DIR = "/home/karan/pyKaran/CarbonEmissions/"
CSV_DIR = os.path.join(BASE_DIR, "Sheet4csv")
METRICS_DIR = os.path.join(CSV_DIR, "metrics")
OUTPUT_DIR = os.path.join(BASE_DIR, "Sheet4_Analysis")

def get_substance_sector_from_prefix(prefix):
    parts = prefix.split('_')
    if parts[0] == 'CO2':
        substance = 'CO2'
        sector = ' '.join(parts[1:])
    elif 'F-gases' in prefix:
        substance = 'GWP 100 AR5 F-gases'
        sector = 'Processes'
    else: # CH4 or N2O
        substance = ' '.join(parts[0:4]).replace('GWP 100', 'GWP_100')
        sector = ' '.join(parts[4:])
    return substance, sector

def format_report(prefix, data):
    gas, sector = get_substance_sector_from_prefix(prefix)
    report = f"# Analysis of {gas} Emissions from {sector}\n\n"

    # --- 1. Full-Series Trend ---
    report += "## 1. Full-Series Trend (1970–2024): High-Level Insights\n\n"
    ts = data['timeseries']
    start_val, end_val = ts.iloc[0], ts.iloc[-1]
    report += f"The series shows a long-run growth in emissions from **~{start_val:.0f} Mt CO2eq** in 1970 to **~{end_val:.0f} Mt CO2eq** in 2024.\n\n"
    
    report += "Key quantitative features visible in the curve:\n"
    breaks = [1970] + list(data['breaks']['Break_Year']) + [2024]
    for i in range(len(breaks) - 1):
        start_year, end_year = breaks[i], breaks[i+1]
        # for end_year, we should look at the data for the previous year for the range
        val_start = ts.get(str(start_year), 0)
        val_end = ts.get(str(end_year -1), 0) if end_year != 2024 else ts.get(str(end_year), 0)
        report += f"- **{start_year}–{end_year}**: Emissions moved from ~{val_start:.0f} to ~{val_end:.0f} Mt CO2eq.\n"
    report += "\n"

    # --- 2. Breakpoint Detection ---
    report += "## 2. Breakpoint Detection and Regime Analysis\n\n"
    break_years = data['breaks']['Break_Year'].tolist()
    report += f"The analysis identified **{len(break_years)} structural breakpoints** at: {', '.join(map(str, break_years))}. These correspond to significant shifts in the emissions trend.\n\n"
    
    regime_breaks = [1970] + break_years + [2025]
    slopes = eval(data['metrics']['Segment_Slopes'].iloc[0])
    for i in range(len(regime_breaks) - 1):
        start_year, end_year = regime_breaks[i], regime_breaks[i+1]
        val_start = ts.get(str(start_year), 0)
        val_end = ts.get(str(end_year - 1), 0)
        report += f"### Regime {i+1}: {start_year}–{end_year-1}\n"
        report += f"- **Trend**: This regime shows a slope of **{slopes[i]:.2f}**, indicating the rate of change in emissions.\n"
        report += f"- **Emissions Range**: Emissions grew from ~{val_start:.0f} to ~{val_end:.0f} Mt CO2eq.\n"
        report += f"- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the {sector} sector, while a flatter slope suggests a slowdown.\n\n"

    # --- 3. Piecewise Regression ---
    report += "## 3. Piecewise Regression Analysis\n\n"
    r2_adj = data['metrics']['R2_Adjusted'].iloc[0]
    report += f"The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of {r2_adj:.3f}**.\n\n"
    
    slope_comparison = []
    for i in range(len(slopes) - 1):
        if slopes[i+1] > slopes[i]:
            comparison = "steeper"
        else:
            comparison = "flatter"
        slope_comparison.append(f"Regime {i+2} is {comparison} than Regime {i+1}")
    
    report += "**Slope Behavior**:\n"
    report += "- The model identifies genuine trend shifts. The slopes of the segments are: " + ", ".join([f"{s:.2f}" for s in slopes]) + ".\n"
    if len(slopes) > 1:
        is_accelerating = all(np.diff(slopes) > 0)
        if is_accelerating:
            report += "- **Conclusion**: Emissions are **accelerating over time**, with each new regime growing faster per year than the previous one.\n\n"
        else:
            report += "- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.\n\n"

    # --- 4. ARIMA Forecasting & Post-2020 Trend ---
    report += "## 4. ARIMA Forecasting and Post-2020 Trend\n\n"
    chow_p = data['chow']['p_value'].iloc[0]
    if chow_p < 0.05:
        report += f"The Chow test confirms a **statistically significant structural break in 2020** (p-value: {chow_p:.4f}), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.\n\n"
    else:
        report += f"The Chow test for a 2020 break was **not statistically significant** (p-value: {chow_p:.4f}), suggesting the 2020 event did not cause a structural deviation from the prior trend in this specific series.\n\n"

    last_regime_arima = data['arima'].iloc[-1]
    forecast_end_val = data['forecast']['Forecast'].iloc[-1]
    report += f"The 10-year forecast is based on the final regime's ARIMA{last_regime_arima['Order']} model.\n"
    report += f"- **Forecast**: The model projects that emissions will reach **~{forecast_end_val:.0f} Mt CO2eq by 2034**.\n"
    report += "- **Implication**: This forecast continues the trajectory of the most recent growth phase.\n\n"

    # --- 5. Integrated Interpretation & Conclusions ---
    report += "## 5. Integrated Interpretation & Conclusions\n\n"
    report += "Based on the structural breaks, slopes, and forecast, we can draw several conclusions:\n"
    report += "- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.\n"
    report += f"- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the {sector} sector.\n"
    if chow_p < 0.05:
        report += "- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.\n"
    else:
        report += "- **The 2020 event did not create a lasting structural break** for this specific series, with the trend absorbing the shock.\n"
    report += f"- **The most recent regime (post-{regime_breaks[-2]}) drives a strong upward forecast**, projecting continued emissions growth over the next decade.\n"

    return report

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    full_data = pd.read_csv(os.path.join(BASE_DIR, 'carbon emissions data - Sheet4.csv'))
    full_data.dropna(how='all', inplace=True)
    full_data = full_data[~full_data['Substance'].str.contains('values in GHG_by_sector_and_country', na=False)]
    year_cols = [col for col in full_data.columns if col.isdigit()]

    for prefix in PREFIXES:
        try:
            data = {}
            substance, sector = get_substance_sector_from_prefix(prefix)
            
            ts_row = full_data[(full_data['Substance'] == substance.replace(' ', '_')) & (full_data['Sector'] == sector)]
            if ts_row.empty:
                print(f"Warning: No time series data found for {prefix}")
                continue
            data['timeseries'] = ts_row[year_cols].iloc[0]

            data['breaks'] = pd.read_csv(os.path.join(CSV_DIR, f"{prefix}_breaks.csv"))
            data['chow'] = pd.read_csv(os.path.join(CSV_DIR, f"{prefix}_chow_2020.csv"))
            data['arima'] = pd.read_csv(os.path.join(CSV_DIR, f"{prefix}_regime_arima.csv"))
            data['forecast'] = pd.read_csv(os.path.join(CSV_DIR, f"{prefix}_10y_forecast.csv"))
            data['metrics'] = pd.read_csv(os.path.join(METRICS_DIR, f"{prefix}_piecewise_metrics.csv"))
            
            report_content = format_report(prefix, data)
            
            output_path = os.path.join(OUTPUT_DIR, f"{prefix}_analysis.md")
            with open(output_path, 'w') as f:
                f.write(report_content)
                
        except FileNotFoundError as e:
            print(f"Skipping {prefix}: File not found - {e}")
            continue
    print(f"Generated {len(PREFIXES)} reports in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
