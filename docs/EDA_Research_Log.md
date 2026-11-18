# CERN Proton Collision Anomaly Detection

## Exploratory Data Analysis (EDA)

### 1. Dataset Overview

The dataset contains 21,726 collision events and 17 attributes derived from CERN CMS proton collision data.

### 2. Initial Data Audit

The following checks were performed:

| Check | Result |
|---|---|
| Dataset dimensions | 21,726 rows × 17 columns |
| Data types | All columns are numeric |
| Missing values | 0 |
| Duplicate rows | 0 |

### 3. Initial Statistical Analysis

Descriptive statistics were generated using Pandas `describe()` to examine the distributions and ranges of numerical features.

Initial observations:

- MR ranges from approximately 29.99 to 2433.82.
- Rsq ranges from approximately 0.000009 to 0.7637.
- HT ranges from approximately 120.94 to 1462.63.
- MET ranges from approximately 0.10 to 423.14.

These ranges require further investigation through visualization and domain-aware analysis.

### 4. Next Analysis Steps

- Visualize numerical feature distributions.
- Investigate skewness and extreme values.
- Examine potential outliers.
- Interpret unusual observations in their physical context.

### 5. MR Distribution Analysis

**Visualization:** Histogram of MR

**Observation:**

The MR feature exhibits a right-skewed distribution, with most observations concentrated at relatively lower values and a long tail extending toward higher values.

**Statistical Evidence:**

- Mean: 351.98
- Median: 292.91
- Maximum: 2433.82

The mean being greater than the median supports the observed positive skewness.

**Interpretation:**

A small number of events have substantially higher MR values than the majority of observations. These events require further investigation and should not automatically be classified as anomalies.

**Next Step:**

Investigate extreme values using additional statistical and visualization techniques.

### 6. MR Boxplot Analysis

**Method:** Boxplot using the 1.5 × IQR rule.

**Statistical Findings:**

- Q1: 229.79
- Median: 292.91
- Q3: 406.88
- IQR: 177.09
- Upper Fence: 672.52
- Percentage of observations above the Upper Fence: 6.49%

**Interpretation:**

Approximately 6.49% of the observations have MR values above the statistical upper fence. These observations are considered potential statistical outliers according to the 1.5 × IQR rule.

However, statistical outliers are not necessarily physically anomalous events. Further investigation using multiple features and physics-aware analysis is required.

**Next Step:**

Investigate the distributions of additional physical variables, particularly Rsq, HT, and MET.

### 7. Rsq Distribution Analysis

**Visualization:** Histogram of Rsq

**Observation:**

The Rsq distribution exhibits positive (right) skewness, indicating that most observations are concentrated at relatively low values, while fewer observations extend toward higher values.

**Interpretation:**

The distribution is asymmetric, with a longer tail toward higher Rsq values. These higher values may represent statistically unusual events, but they should not automatically be classified as anomalies.

Further investigation is needed to understand the relationship between Rsq and other physical variables, particularly MR.

**Next Step:**

Analyze the Rsq distribution using a boxplot and investigate potential statistical outliers.

### 8. Rsq Boxplot Analysis

**Visualization:** Boxplot of Rsq

**Observations:**

- The distribution is strongly right-skewed.
- The interquartile range is concentrated near zero, indicating that the middle 50% of observations have relatively low and closely grouped Rsq values.
- Several observations extend beyond the upper whisker.
- A small number of extreme values appear near 0.72–0.77.

**Interpretation:**

The boxplot indicates that Rsq contains a substantial number of statistically distant observations according to the boxplot's outlier rule.

However, these observations cannot automatically be considered physically anomalous events. Rsq is a Razor kinematic variable, not a machine learning model performance metric.

Further investigation should consider its relationship with MR and other event-level features.

**Next Step:**

Calculate the IQR-based upper fence and quantify the percentage of potential statistical outliers.


