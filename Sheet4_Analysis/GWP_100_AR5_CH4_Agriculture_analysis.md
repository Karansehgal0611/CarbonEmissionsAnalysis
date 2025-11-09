# Analysis of GWP_100 AR5 CH4 Emissions from Agriculture

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~348 Mt CO2eq** in 1970 to **~572 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–1976**: Emissions moved from ~348 to ~369 Mt CO2eq.
- **1976–1989**: Emissions moved from ~368 to ~454 Mt CO2eq.
- **1989–2019**: Emissions moved from ~462 to ~540 Mt CO2eq.
- **2019–2024**: Emissions moved from ~542 to ~572 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 1976, 1989, 2019. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–1975
- **Trend**: This regime shows a slope of **3.90**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~348 to ~369 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Agriculture sector, while a flatter slope suggests a slowdown.

### Regime 2: 1976–1988
- **Trend**: This regime shows a slope of **6.72**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~368 to ~454 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Agriculture sector, while a flatter slope suggests a slowdown.

### Regime 3: 1989–2018
- **Trend**: This regime shows a slope of **2.81**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~462 to ~540 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Agriculture sector, while a flatter slope suggests a slowdown.

### Regime 4: 2019–2024
- **Trend**: This regime shows a slope of **5.77**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~542 to ~572 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Agriculture sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.994**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 3.90, 6.72, 2.81, 5.77.
- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test for a 2020 break was **not statistically significant** (p-value: 0.2815), suggesting the 2020 event did not cause a structural deviation from the prior trend in this specific series.

The 10-year forecast is based on the final regime's ARIMA(3, 2, 0) model.
- **Forecast**: The model projects that emissions will reach **~629 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Agriculture sector.
- **The 2020 event did not create a lasting structural break** for this specific series, with the trend absorbing the shock.
- **The most recent regime (post-2019) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
