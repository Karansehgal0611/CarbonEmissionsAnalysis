import pandas as pd
import numpy as np

def analyze_emissions_data(file_path):
    df = pd.read_csv(file_path)
    
    # Drop empty rows and the last few footer rows
    df.dropna(how='all', inplace=True)
    df = df[~df['Substance'].str.contains('values in GHG_by_sector_and_country', na=False)]


    # Get year columns
    year_cols = [col for col in df.columns if col.isdigit()]
    
    report = ""

    for substance in df['Substance'].unique():
        report += f"# Analysis for {substance}\n\n"
        substance_df = df[df['Substance'] == substance]
        
        for index, row in substance_df.iterrows():
            sector = row['Sector']
            report += f"## Sector: {sector}\n\n"
            
            time_series = row[year_cols].astype(float)
            
            # Summary Statistics
            total_emissions = time_series.sum()
            mean_emissions = time_series.mean()
            median_emissions = time_series.median()
            min_emissions = time_series.min()
            max_emissions = time_series.max()
            min_year = time_series.idxmin()
            max_year = time_series.idxmax()
            
            report += "### Summary Statistics\n\n"
            report += f"- **Total Emissions (1970-2024):** {total_emissions:.2f} Mt CO2eq\n"
            report += f"- **Average Yearly Emissions:** {mean_emissions:.2f} Mt CO2eq/yr\n"
            report += f"- **Median Yearly Emissions:** {median_emissions:.2f} Mt CO2eq/yr\n"
            report += f"- **Highest Emissions:** {max_emissions:.2f} Mt CO2eq/yr (in {max_year})\n"
            report += f"- **Lowest Emissions:** {min_emissions:.2f} Mt CO2eq/yr (in {min_year})\n\n"
            
            # Trend Analysis
            start_value = time_series.iloc[0]
            end_value = time_series.iloc[-1]
            num_years = len(time_series) - 1
            
            overall_growth = end_value - start_value
            
            # Calculate CAGR, handle zero start value
            if start_value > 0:
                cagr = ((end_value / start_value) ** (1 / num_years)) - 1
            else:
                cagr = float('inf') if end_value > 0 else 0

            report += "### Trend Analysis (1970-2024)\n\n"
            report += f"- **Emissions in 1970:** {start_value:.2f} Mt CO2eq/yr\n"
            report += f"- **Emissions in 2024:** {end_value:.2f} Mt CO2eq/yr\n"
            report += f"- **Overall Growth:** {overall_growth:.2f} Mt CO2eq/yr\n"
            report += f"- **Compound Annual Growth Rate (CAGR):** {cagr:.2%}\n\n"
            
    return report

if __name__ == '__main__':
    report_content = analyze_emissions_data('/home/karan/pyKaran/CarbonEmissions/carbon emissions data - Sheet4.csv')
    with open('/home/karan/pyKaran/CarbonEmissions/emissions_analysis_report.md', 'w') as f:
        f.write(report_content)
