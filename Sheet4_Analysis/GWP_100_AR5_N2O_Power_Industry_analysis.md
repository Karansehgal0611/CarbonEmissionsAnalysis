# Analysis of GWP_100 AR5 N2O Emissions from Power Industry

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~1 Mt CO2eq** in 1970 to **~25 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–2005**: Emissions moved from ~1 to ~4 Mt CO2eq.
- **2005–2014**: Emissions moved from ~5 to ~17 Mt CO2eq.
- **2014–2020**: Emissions moved from ~19 to ~19 Mt CO2eq.
- **2020–2024**: Emissions moved from ~17 to ~25 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 2005, 2014, 2020. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–2004
- **Trend**: This regime shows a slope of **0.11**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~1 to ~4 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Power Industry sector, while a flatter slope suggests a slowdown.

### Regime 2: 2005–2013
- **Trend**: This regime shows a slope of **1.63**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~5 to ~17 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Power Industry sector, while a flatter slope suggests a slowdown.

### Regime 3: 2014–2019
- **Trend**: This regime shows a slope of **-0.03**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~19 to ~19 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Power Industry sector, while a flatter slope suggests a slowdown.

### Regime 4: 2020–2024
- **Trend**: This regime shows a slope of **1.74**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~17 to ~25 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Power Industry sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.994**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 0.11, 1.63, -0.03, 1.74.
- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test confirms a **statistically significant structural break in 2020** (p-value: 0.0015), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.

The 10-year forecast is based on the final regime's ARIMA(2, 2, 0) model.
- **Forecast**: The model projects that emissions will reach **~43 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Power Industry sector.
- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.
- **The most recent regime (post-2020) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
