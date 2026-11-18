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