# Analysis of CO2 Emissions from Transport

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~44 Mt CO2eq** in 1970 to **~344 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–1987**: Emissions moved from ~44 to ~54 Mt CO2eq.
- **1987–2004**: Emissions moved from ~57 to ~100 Mt CO2eq.
- **2004–2017**: Emissions moved from ~108 to ~269 Mt CO2eq.
- **2017–2024**: Emissions moved from ~291 to ~344 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 1987, 2004, 2017. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–1986
- **Trend**: This regime shows a slope of **0.69**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~44 to ~54 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

### Regime 2: 1987–2003
- **Trend**: This regime shows a slope of **2.89**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~57 to ~100 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

### Regime 3: 2004–2016
- **Trend**: This regime shows a slope of **13.89**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~108 to ~269 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

### Regime 4: 2017–2024
- **Trend**: This regime shows a slope of **6.81**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~291 to ~344 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Transport sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.994**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 0.69, 2.89, 13.89, 6.81.
- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test confirms a **statistically significant structural break in 2020** (p-value: 0.0021), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.

The 10-year forecast is based on the final regime's ARIMA(0, 2, 1) model.
- **Forecast**: The model projects that emissions will reach **~420 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Transport sector.
- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.
- **The most recent regime (post-2017) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
