# Analysis of GWP_100 AR5 CH4 Emissions from Waste

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~50 Mt CO2eq** in 1970 to **~135 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–1994**: Emissions moved from ~50 to ~73 Mt CO2eq.
- **1994–2010**: Emissions moved from ~74 to ~101 Mt CO2eq.
- **2010–2020**: Emissions moved from ~103 to ~123 Mt CO2eq.
- **2020–2024**: Emissions moved from ~124 to ~135 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 1994, 2010, 2020. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–1993
- **Trend**: This regime shows a slope of **1.02**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~50 to ~73 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Waste sector, while a flatter slope suggests a slowdown.

### Regime 2: 1994–2009
- **Trend**: This regime shows a slope of **1.81**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~74 to ~101 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Waste sector, while a flatter slope suggests a slowdown.

### Regime 3: 2010–2019
- **Trend**: This regime shows a slope of **2.17**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~103 to ~123 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Waste sector, while a flatter slope suggests a slowdown.

### Regime 4: 2020–2024
- **Trend**: This regime shows a slope of **2.71**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~124 to ~135 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Waste sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.999**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 1.02, 1.81, 2.17, 2.71.
- **Conclusion**: Emissions are **accelerating over time**, with each new regime growing faster per year than the previous one.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test confirms a **statistically significant structural break in 2020** (p-value: 0.0000), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.

The 10-year forecast is based on the final regime's ARIMA(3, 0, 0) model.
- **Forecast**: The model projects that emissions will reach **~127 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Waste sector.
- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.
- **The most recent regime (post-2020) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
