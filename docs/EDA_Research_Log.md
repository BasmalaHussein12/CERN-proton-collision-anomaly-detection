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

### 9. Rsq Statistical Outlier Analysis

**Method:** Interquartile Range (IQR) using the 1.5 × IQR rule.

**Results:**

| Metric | Value |
|---|---:|
| Q1 | 0.007907 |
| Median | 0.016817 |
| Q3 | 0.031612 |
| IQR | 0.023705 |
| Upper Fence | 0.067170 |
| Potential Outliers | 1,001 |
| Percentage | 4.61% |

**Interpretation:**

A total of 1,001 observations (approximately 4.61% of the dataset) have Rsq values above the statistical upper fence.

These observations are potential statistical outliers, not confirmed physical anomalies.

### 10. Initial Comparison: MR vs Rsq

Both MR and Rsq exhibit right-skewed distributions.

Using the 1.5 × IQR rule, approximately 6.49% of observations were identified above the MR upper fence, compared with 4.61% above the Rsq upper fence.

This comparison highlights differences in their univariate distributions. It does not establish whether the same collision events are unusual across both features.


### Rsq Statistical Outlier Analysis

The Interquartile Range (IQR) method was applied to identify potentially unusual values in the Rsq feature.

**Results:**
- Q1: 0.00791
- Q3: 0.03161
- IQR: 0.02371
- Upper Fence: 0.06717
- Number of potential outliers: 1,001
- Percentage of potential outliers: 4.61%

**Interpretation:**

Approximately 4.61% of the observations have Rsq values above the upper IQR fence. This indicates the presence of a relatively small group of observations with unusually high Rsq values compared to the central distribution.

However, these observations should not automatically be classified as physical anomalies or removed from the dataset. The IQR method identifies statistical outliers in a single feature and does not establish whether an event is physically anomalous.

Further multivariate analysis is required to investigate these observations in relation to other kinematic features.

## 2. Dataset Overview and Initial Data Quality Assessment

### 2.1 Dataset Overview

The dataset contains 21,726 observations and 17 columns.

The features include event identifiers, derived physics variables, energy measurements, momentum components, event activity variables, and jet multiplicity information.

### 2.2 Initial Data Quality

The initial inspection revealed:

- No missing values across the 17 columns.
- No completely duplicated rows.
- All numerical columns have valid numeric data types.

These findings indicate complete data coverage at the initial inspection stage. However, further physical consistency and event identifier checks are still required.

### 2.3 Initial Statistical Observations

**MR and Rsq**

Both variables show a noticeable difference between their means and medians, suggesting potentially right-skewed distributions.

For Rsq, the IQR method identified 1,001 potential upper outliers, representing approximately 4.61% of the observations.

**Energy Variables**

E1 and E2 have means greater than their medians, suggesting right-skewed distributions with relatively high values in their upper tails.

**Momentum Components**

The momentum components contain both positive and negative values, which is consistent with their directional nature.

**HT and MET**

Both variables exhibit relatively large maximum values compared with their upper quartiles. Their distributions require further investigation.

**Jet Multiplicity**

nJets ranges from 2 to 7, while nBJets ranges from 0 to 2. The third quartile of nBJets is zero, indicating that at least 75% of the observations have zero b-tagged jets.

### 2.4 Next Investigation Steps

- Extended statistical analysis using skewness and additional quantiles.
- Zero and negative value investigation.
- Complete univariate analysis of all physics features.
- Multivariate correlation analysis.
- Physics-based consistency checks.

### Univariate Distribution Observations

The univariate analysis revealed several patterns across the dataset:

1. **Jet Multiplicity:** `nJets` is concentrated around low multiplicities, with 2 jets being the most frequent observation. The frequency decreases as the number of jets increases.

2. **B-tagged Jet Multiplicity:** `nBJets` is highly imbalanced, with approximately 94.89% of events containing zero b-tagged jets.

3. **Energy and Event Activity Variables:** `MR`, `Rsq`, `E1`, `E2`, `HT`, and `MET` exhibit varying degrees of positive skewness and extended upper tails. Their extreme values require further investigation rather than immediate removal.

4. **Momentum Components:** The momentum components contain both positive and negative values, reflecting directional information. Their distribution shapes and symmetry should be investigated further before making physical interpretations.

5. **Potential Extreme Values:** Several variables contain observations far beyond their central ranges. These observations will be examined using statistical methods and, where possible, physics-based consistency checks.

At this stage, no observations are classified as confirmed physical anomalies or new-physics signals.

### Bimodal Distribution in Transverse Momentum Components

During the univariate analysis, I observed a bimodal pattern in both `Px1` and `Py1`.

The KDE visualizations show two apparent density peaks, approximately around negative and positive values, with a local minimum near zero.

This pattern is worth investigating further. However, I cannot yet attribute it to a specific physical process or reconstruction mechanism.

Further analysis will include:
- Quantifying the locations of local density maxima.
- Checking the sensitivity of the KDE shape to bandwidth selection.
- Investigating the relationship between `Px1` and `Py1`.
- Comparing the distributions with other kinematic variables.

At this stage, bimodality is treated as a statistical observation rather than evidence of a particular physical phenomenon.

**Basmala Hussein**
