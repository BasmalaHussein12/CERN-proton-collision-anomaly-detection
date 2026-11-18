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
