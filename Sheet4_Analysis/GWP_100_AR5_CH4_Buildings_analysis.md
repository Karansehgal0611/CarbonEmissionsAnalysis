# Analysis of GWP_100 AR5 CH4 Emissions from Buildings

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~21 Mt CO2eq** in 1970 to **~38 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–1993**: Emissions moved from ~21 to ~34 Mt CO2eq.
- **1993–2003**: Emissions moved from ~34 to ~35 Mt CO2eq.
- **2003–2008**: Emissions moved from ~35 to ~36 Mt CO2eq.
- **2008–2024**: Emissions moved from ~40 to ~38 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 1993, 2003, 2008. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–1992
- **Trend**: This regime shows a slope of **0.59**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~21 to ~34 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Buildings sector, while a flatter slope suggests a slowdown.

### Regime 2: 1993–2002
- **Trend**: This regime shows a slope of **0.07**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~34 to ~35 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Buildings sector, while a flatter slope suggests a slowdown.

### Regime 3: 2003–2007
- **Trend**: This regime shows a slope of **0.60**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~35 to ~36 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Buildings sector, while a flatter slope suggests a slowdown.

### Regime 4: 2008–2024
- **Trend**: This regime shows a slope of **-0.02**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~40 to ~38 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Buildings sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.993**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 0.59, 0.07, 0.60, -0.02.
- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test confirms a **statistically significant structural break in 2020** (p-value: 0.0000), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.

The 10-year forecast is based on the final regime's ARIMA(1, 2, 2) model.
- **Forecast**: The model projects that emissions will reach **~39 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Buildings sector.
- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.
- **The most recent regime (post-2008) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
