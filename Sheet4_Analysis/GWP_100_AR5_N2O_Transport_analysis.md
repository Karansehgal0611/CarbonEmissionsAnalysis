# Analysis of GWP_100 AR5 N2O Emissions from Transport

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~1 Mt CO2eq** in 1970 to **~7 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–1998**: Emissions moved from ~1 to ~3 Mt CO2eq.
- **1998–2005**: Emissions moved from ~3 to ~3 Mt CO2eq.
- **2005–2010**: Emissions moved from ~3 to ~5 Mt CO2eq.
- **2010–2024**: Emissions moved from ~5 to ~7 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 1998, 2005, 2010. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–1997
- **Trend**: This regime shows a slope of **0.07**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~1 to ~3 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

### Regime 2: 1998–2004
- **Trend**: This regime shows a slope of **-0.00**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~3 to ~3 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

### Regime 3: 2005–2009
- **Trend**: This regime shows a slope of **0.53**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~3 to ~5 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

### Regime 4: 2010–2024
- **Trend**: This regime shows a slope of **0.14**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~5 to ~7 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.988**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 0.07, -0.00, 0.53, 0.14.
- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test for a 2020 break was **not statistically significant** (p-value: 0.0647), suggesting the 2020 event did not cause a structural deviation from the prior trend in this specific series.

The 10-year forecast is based on the final regime's ARIMA(3, 2, 3) model.
- **Forecast**: The model projects that emissions will reach **~12 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Transport sector.
- **The 2020 event did not create a lasting structural break** for this specific series, with the trend absorbing the shock.
- **The most recent regime (post-2010) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
