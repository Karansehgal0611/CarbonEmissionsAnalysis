# Analysis of CO2 Emissions from Industrial Combustion

## 1. Full-Series Trend (1970–2024): High-Level Insights

The series shows a long-run growth in emissions from **~63 Mt CO2eq** in 1970 to **~689 Mt CO2eq** in 2024.

Key quantitative features visible in the curve:
- **1970–2004**: Emissions moved from ~63 to ~200 Mt CO2eq.
- **2004–2015**: Emissions moved from ~210 to ~500 Mt CO2eq.
- **2015–2020**: Emissions moved from ~516 to ~555 Mt CO2eq.
- **2020–2024**: Emissions moved from ~517 to ~689 Mt CO2eq.

## 2. Breakpoint Detection and Regime Analysis

The analysis identified **3 structural breakpoints** at: 2004, 2015, 2020. These correspond to significant shifts in the emissions trend.

### Regime 1: 1970–2003
- **Trend**: This regime shows a slope of **4.60**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~63 to ~200 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

### Regime 2: 2004–2014
- **Trend**: This regime shows a slope of **29.58**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~210 to ~500 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

### Regime 3: 2015–2019
- **Trend**: This regime shows a slope of **3.33**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~516 to ~555 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

### Regime 4: 2020–2024
- **Trend**: This regime shows a slope of **35.09**, indicating the rate of change in emissions.
- **Emissions Range**: Emissions grew from ~517 to ~689 Mt CO2eq.
- **Inference**: A change in slope from the previous regime suggests a structural shift. A steeper slope indicates accelerated emissions growth, likely tied to increased activity in the Industrial Combustion sector, while a flatter slope suggests a slowdown.

## 3. Piecewise Regression Analysis

The piecewise regression model provides a strong fit to the data, with an **Adjusted R-squared of 0.997**.

**Slope Behavior**:
- The model identifies genuine trend shifts. The slopes of the segments are: 4.60, 29.58, 3.33, 35.09.
- **Conclusion**: The trend shows **variable growth**, not a simple acceleration, with shifts in growth rate between regimes.

## 4. ARIMA Forecasting and Post-2020 Trend

The Chow test confirms a **statistically significant structural break in 2020** (p-value: 0.0009), likely corresponding to the COVID-19 pandemic's impact and subsequent recovery.

The 10-year forecast is based on the final regime's ARIMA(1, 2, 0) model.
- **Forecast**: The model projects that emissions will reach **~1097 Mt CO2eq by 2034**.
- **Implication**: This forecast continues the trajectory of the most recent growth phase.

## 5. Integrated Interpretation & Conclusions

Based on the structural breaks, slopes, and forecast, we can draw several conclusions:
- **Emissions growth is not steady; it occurs in distinct phases**, with statistically significant breaks indicating different growth rates over time.
- **Major accelerations** appear to correspond with the identified breakpoints, suggesting periods of increased industrial or economic activity affecting the Industrial Combustion sector.
- **The break at 2020 is real and impactful**, causing a temporary deviation before emissions rebounded, often onto a new trajectory.
- **The most recent regime (post-2020) drives a strong upward forecast**, projecting continued emissions growth over the next decade.
