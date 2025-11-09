# Analysis of GWP_100 AR5 CH4 Emissions from Industrial Combustion

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~1 Mt CO2eq** in 1970 to **~4 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–1992**: Emissions moved from ~1 to ~1 Mt CO2eq.
- **1992–2005**: Emissions moved from ~1 to ~2 Mt CO2eq.
- **2005–2020**: Emissions moved from ~2 to ~3 Mt CO2eq.
- **2020–2024**: Emissions moved from ~4 to ~4 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 1992, 2005, 2020. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–1991
- **Trend**: This regime shows a slope of **0.01**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~1 to ~1 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

### Regime 2: 1992–2004
- **Trend**: This regime shows a slope of **0.06**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~1 to ~2 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

### Regime 3: 2005–2019
- **Trend**: This regime shows a slope of **0.13**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~2 to ~3 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

### Regime 4: 2020–2024
- **Trend**: This regime shows a slope of **0.21**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~4 to ~4 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.998**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 0.01, 0.06, 0.13, 0.21.
- **Conclusion**: Emissions are **accelerating over time**, with each new regime growing faster per year than the previous one.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test confirms a **statistically significant structural break in 2020** (p-value: 0.0000), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.

The 10-year forecast is based on the final regime's ARIMA(3, 0, 1) model.
- **Forecast**: The model projects that emissions will reach **~4 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Industrial Combustion sector.
- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.
- **The most recent regime (post-2020) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
