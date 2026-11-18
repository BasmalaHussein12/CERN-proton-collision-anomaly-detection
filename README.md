## Planned Methodology

This project will investigate three complementary approaches to unsupervised anomaly detection in CERN proton collision data.

### 1. Principal Component Analysis (PCA)

**Purpose:** Dimensionality reduction and exploratory analysis.

PCA will be used to transform correlated features into a lower-dimensional representation while preserving as much variance as possible.

It will help explore the structure of collision events, identify dominant sources of variation, and visualize potential patterns in the dataset.

PCA will primarily serve as an exploratory and analytical tool rather than a standalone anomaly detection method.

### 2. Isolation Forest

**Purpose:** Baseline unsupervised anomaly detection.

Isolation Forest identifies observations that can be isolated more easily than others through random partitioning.

It will serve as an initial baseline for identifying potentially unusual collision events.

Experiments will investigate the effects of different contamination settings, feature subsets, and preprocessing choices on the detected observations.

### 3. Autoencoder

**Purpose:** Neural network-based anomaly detection.

An autoencoder is a neural network trained to reconstruct its input data.

The model will learn representations of common patterns in the collision dataset. Reconstruction errors will then be investigated as potential indicators of unusual observations.

This approach will be explored after establishing simpler baselines, with particular attention to model architecture, training stability, and reconstruction error distributions.

## Evaluation and Interpretation

The project will investigate the reliability, consistency, and interpretability of the detected events.

Planned experiments include:

- **Model comparison:** Compare anomaly scores, detection overlap, and the characteristics of events identified by different approaches.
- **Stability analysis:** Investigate how detection results change across random seeds, training samples, and model configurations.
- **Feature selection:** Examine how different physical feature subsets affect detection performance and identified events.
- **Preprocessing analysis:** Study the effects of feature scaling, skewed distributions, and other preprocessing choices.
- **Physics-aware interpretation:** Investigate the physical characteristics and relationships of flagged events, including MR, Rsq, HT, and MET.
- **Sensitivity analysis:** Examine how detection thresholds and Isolation Forest contamination settings influence the results.

## Data Preparation Considerations

Before model training, the project will investigate:

- The role of event identifiers such as Run, Lumi, and Event.
- The selection of physically meaningful input features.
- Feature scaling and distribution transformations where appropriate.
- The handling of extreme values without automatically removing potentially meaningful rare events.

## Important Note

An anomaly score indicates that an observation differs from patterns learned by a model. It does not, by itself, establish that the event represents a new particle or a scientifically meaningful discovery.

The methodology and evaluation strategy may be refined as the dataset structure, feature definitions, and available reference labels are investigated.
