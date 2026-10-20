## Planned Methodology

This project will explore three complementary approaches to unsupervised anomaly detection in CERN proton collision data.

### 1. Principal Component Analysis (PCA)

**Purpose:** Dimensionality reduction and data exploration.

PCA helps reduce the number of features while preserving as much of the original data's variance as possible. It will help us understand the structure of the dataset and explore lower-dimensional representations of collision events.

### 2. Isolation Forest

**Purpose:** Detecting potentially unusual data points.

Isolation Forest identifies observations that can be isolated relatively easily from the rest of the dataset. We will use it as an initial anomaly detection baseline and investigate the characteristics of the events it flags.

### 3. Autoencoder

**Purpose:** Neural network-based anomaly detection.

An autoencoder is a neural network trained to reconstruct its input data. We will investigate whether unusually high reconstruction errors can help identify potentially anomalous collision events.

This approach will be explored after establishing simpler baselines.

## Evaluation and Interpretation

Beyond training models, this project will investigate how reliable and interpretable their results are.

Planned experiments include:

- **Model comparison:** Compare anomaly scores and the events identified by different approaches.
- **Stability analysis:** Investigate how results change across random seeds and training samples.
- **Feature selection:** Examine how different input features affect anomaly detection.
- **Preprocessing analysis:** Study the effects of scaling and other preprocessing choices.
- **Interpretation:** Analyze the characteristics of flagged events and investigate whether their patterns have plausible physical explanations.

### Important Note

An anomaly score indicates that an observation differs from patterns learned by a model. It does not, by itself, establish that the event represents a new particle or a scientifically meaningful discovery.

The methodology and evaluation strategy may be refined as the dataset structure, feature definitions, and available reference labels are investigated.