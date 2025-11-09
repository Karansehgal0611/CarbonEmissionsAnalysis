# Analysis of India's Sectoral Greenhouse Gas Emissions (1970-2024)

## 1. Project Overview

This repository contains a deep-dive analysis of India's greenhouse gas emissions across 24 distinct sectors from 1970 to 2024. The analysis moves beyond high-level trends to uncover the underlying narratives of growth, stagnation, and technological change that define each sector's unique emissions trajectory. By identifying statistically significant structural breaks in the historical data, we can pinpoint key inflection points and understand the real-world economic and policy shifts driving India's emissions profile.

This work was performed through a combination of statistical analysis in Python (using pandas and statsmodels) and detailed interpretation of the resulting time-series data, breakpoints, and forecasts.

## 2. Executive Summary: Key Findings

A comprehensive analysis of all 24 sectors reveals several critical, overarching narratives:

1.  **The Industrial Core is in Overdrive:** The primary drivers of India's emissions—**CO2 from Power, Industry, and Processes**—are not just growing, they are in a state of compounding acceleration. The post-COVID rebound has been particularly intense, pushing these sectors onto their steepest growth trajectories in history.

2.  **A Tale of Two Growth Models:** A major divergence has appeared. While the industrial core accelerates, **CO2 from Transport** tells a hopeful story of "peak growth" being passed, with a significant, policy-driven deceleration in its growth rate since 2017. This proves that bending the curve is possible.

3.  **The Next Wave of Challenges is Here:** The data reveals the next frontier of climate challenges. **F-Gases** from the "great Indian cooling boom" and emissions from **Waste** are on purely accelerative "hockey stick" curves, tightly coupled with rising prosperity and consumption.

4.  **Hidden Successes Point the Way:** Buried in the smaller data series are clear success stories. The near-total stagnation of **methane (CH4) from new gas buildings** and the moderation of **nitrous oxide (N2O) from transport** show that modern technology and targeted regulations can be highly effective at decoupling growth from emissions.

## 3. Detailed Sectoral Narratives

### The Accelerating Core: Power & Industry
- **Power Industry:** This is the engine of India's emissions growth. Its trajectory is one of relentless acceleration, with each of its four growth phases being significantly steeper than the last. The post-COVID era has the highest growth rate on record.
- **Industrial Combustion & Processes:** These sectors tell a similar story of dramatic, accelerating growth. The post-COVID rebound has been exceptionally strong, indicating a recovery that is both energy- and material-intensive. The growth in process emissions (from cement, etc.) is particularly alarming, as they are often harder to abate.

### The Decoupling Success Story: Transport
- **Transport CO2:** This is the most important positive story in the data. After a "golden age" of explosive growth from 2004-2016, the rate of emissions growth was **cut in half** from 2017 onwards. This strongly suggests that policies like stricter fuel efficiency norms (BS-IV to BS-VI) and infrastructure like metro rail have successfully "bent the curve."

### The Urbanization Proxies: Waste & F-Gases
- **Waste (CH4 & N2O):** Emissions from waste are a story of pure, unchecked acceleration. Tightly coupled with urbanization and consumption, the growth rate has consistently increased with each new economic phase.
- **F-Gases:** This is a classic "hockey stick" curve. After decades of being negligible, emissions exploded upwards after 2007, a direct consequence of the mass adoption of air conditioning and refrigeration. This is a direct proxy for rising prosperity.

### The Agricultural Giants: Methane & N2O
- **Agriculture (CH4 & N2O):** As massive sources of methane and N2O, their growth is like a "heavy tanker"—large in scale but slower-moving and more volatile than CO2 trends. The data reveals distinct phases tied to agricultural policy (the Green Revolution boom, a long 30-year moderation, and a recent, concerning re-acceleration).

## 4. Repository Structure

The repository is organized into several directories, separating raw data, generated data, plots, analysis scripts, and final reports.

```
/
├── carbon emissions data - Sheet[1-5].csv # Primary raw data files for different analyses.
│
├── NB[1-4].ipynb                         # Jupyter Notebooks for exploration, modeling, and plotting.
│
├── Sheet[1-4]csv/                        # Generated tabular data from the analysis of each sheet.
│   ├── *_breaks.csv                      # Detected structural breakpoints for a time series.
│   ├── *_chow_2020.csv                   # Chow test results for the 2020 breakpoint.
│   ├── *_10y_forecast.csv                # 10-year forecast data tables.
│   ├── *_regime_arima.csv                # ARIMA model parameters used for each regime.
│   └── metrics/                          # Subdirectory with detailed piecewise regression metrics.
│
├── Sheet[1-4]Plots/                      # Generated plots and charts from the analysis.
│   ├── *.png                             # Various plots like overall trends, diagnostics, etc.
│   └── Sheet4PeiceWise/                  # Specific plots for the Sheet 4 piecewise model fits and forecasts.
│
├── Sheet4_Deep_Analysis/                 # The core narrative output of this project.
│   ├── *.md                              # Detailed, insightful analysis reports for each of the 24 sectors.
│   └── Comprehensive_Sheet4_Analysis_Report.md # A single, consolidated summary of all findings.
│
├── Sheet4_PDF_Reports/                   # Contains the final PDF versions of all analysis reports.
│
├── README.md                             # The main project documentation file (this file).
│
└── *.py, *.sh, *.tex                     # Various helper scripts and templates created during the analysis.
```

## 5. How to Use This Repository

1.  **Start with the Summary:** For a high-level overview of all findings, read the `Comprehensive_Sheet4_Analysis_Report.md`.
2.  **Dive into Specific Sectors:** To understand the detailed narrative, breakpoints, and forecast for a specific area (e.g., "CO2 from Transport"), explore the corresponding markdown files in the `Sheet4_Deep_Analysis/` directory.
3.  **Explore the Raw Data:** The root directory contains the raw `.csv` files used for the analysis.
4.  **Review the Notebooks:** The `NB*.ipynb` files provide a look into the original code used for the statistical analysis and plotting.