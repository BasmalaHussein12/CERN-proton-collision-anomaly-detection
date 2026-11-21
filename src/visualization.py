import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import seaborn as sns

def plot_mr_distribution(df):

    plt.figure(figsize=(10, 6))

    plt.hist(df["MR"], bins=50)

    plt.xlabel("MR")
    plt.ylabel("Frequency")
    plt.title("Distribution of MR")

    plt.savefig("results/figures/mr_distribution.png",
            dpi=300, bbox_inches="tight")

    plt.show(block=False)
    plt.pause(1)
    plt.close()



def plot_mr_boxplot(df):

    plt.figure(figsize=(10, 5))

    plt.boxplot(df["MR"], orientation="horizontal")

    plt.xlabel("MR")
    plt.title("Boxplot of MR")

    plt.savefig(
        "results/figures/mr_boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show(block=False)
    plt.pause(1)
    plt.close()

def plot_rsq_distribution(df):

    plt.figure(figsize=(10, 6))

    plt.hist(df["Rsq"], bins=50)

    plt.xlabel("Rsq")
    plt.ylabel("Frequency")
    plt.title("Distribution of Rsq")

    plt.savefig(
        "results/figures/rsq_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show(block=False)
    plt.pause(1)
    plt.close()


def plot_rsq_boxplot(df):

    plt.figure(figsize=(10, 5))

    plt.boxplot(df["Rsq"], orientation="horizontal")

    plt.xlabel("Rsq")
    plt.title("Boxplot of Rsq")

    plt.savefig(
        "results/figures/rsq_boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show(block=False)
    plt.pause(1)
    plt.close()

def plot_feature_distribution(df, feature):

    plt.figure(figsize=(10, 6))

    plt.hist(df[feature].dropna(), bins=50)

    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {feature}")

    plt.tight_layout()

    plt.savefig(
        f"results/figures/{feature.lower()}_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def plot_feature_boxplot(df, feature):

    plt.figure(figsize=(10, 5))

    plt.boxplot(
        df[feature].dropna(),
        orientation="horizontal"
    )

    plt.xlabel(feature)
    plt.title(f"Boxplot of {feature}")

    plt.tight_layout()

    plt.savefig(
        f"results/figures/{feature.lower()}_boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def plot_discrete_feature(df, feature):

    counts = df[feature].value_counts().sort_index()

    plt.figure(figsize=(9, 5))

    plt.bar(
        counts.index.astype(str),
        counts.values
    )

    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.title(f"Frequency Distribution of {feature}")

    plt.tight_layout()

    plt.savefig(
        f"results/figures/{feature.lower()}_frequency.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def analyze_all_features(df):

    Path("results/figures").mkdir(
        parents=True,
        exist_ok=True
    )

    continuous_features = [
        "MR", "Rsq",
        "E1", "Px1", "Py1", "Pz1",
        "E2", "Px2", "Py2", "Pz2",
        "HT", "MET"
    ]

    discrete_features = [
        "nJets", "nBJets"
    ]

    for feature in continuous_features:

        print(f"Analyzing {feature}...")

        plot_feature_distribution(df, feature)
        plot_feature_boxplot(df, feature)

    for feature in discrete_features:

        print(f"Analyzing {feature}...")

        plot_discrete_feature(df, feature)

    print("\nUnivariate visualization completed.")

def plot_feature_kde(df, feature):

    plt.figure(figsize=(10, 6))

    sns.kdeplot(data=df, x=feature, fill=True)

    plt.title(f"KDE Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Density")

    plt.savefig(
        f"results/figures/{feature}_kde.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def compare_kde_bandwidths(df, feature):

    plt.figure(figsize=(10, 6))

    bandwidths = [0.5, 1, 1.5, 2]

    for bw in bandwidths:

        sns.kdeplot(
            data=df,
            x=feature,
            bw_adjust=bw,
            cut=0,
            label=f"Bandwidth = {bw}"
        )

    plt.title(f"KDE Bandwidth Comparison - {feature}")
    plt.xlabel(feature)
    plt.ylabel("Density")
    plt.legend()

    plt.savefig(
        f"results/figures/{feature}_kde_bandwidth.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

if __name__ == "__main__":

    from src.data_loader import load_data

    df = load_data()

    # Visualizations
    analyze_all_features(df)

    # Rsq Outlier Analysis
    q1 = df["Rsq"].quantile(0.25)
    q3 = df["Rsq"].quantile(0.75)

    iqr = q3 - q1

    upper_fence = q3 + 1.5 * iqr

    potential_outliers = df[df["Rsq"] > upper_fence]

    print("Rsq Q1:", q1)
    print("Rsq Q3:", q3)
    print("Rsq IQR:", iqr)
    print("Upper Fence:", upper_fence)

    print("Number of Potential Outliers:", len(potential_outliers))

    print(
        "Percentage:",
        len(potential_outliers) / len(df) * 100
    )

    # Feature Inventory

    print("\n========== DATASET OVERVIEW ==========")

    print("Dataset Shape:", df.shape)

    print("\n========== FEATURE NAMES ==========")
    print(df.columns.tolist())

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    print("\n========== DATA QUALITY ==========")

    inventory = pd.DataFrame({
        "Data Type": df.dtypes,
        "Unique Values": df.nunique(),
        "Missing Values": df.isnull().sum(),
        "Missing Percentage": (
            df.isnull().mean() * 100
        )
    })

    print(inventory)

    print("\n========== DUPLICATES ==========")
    print("Duplicate Rows:", df.duplicated().sum())

    print("\n========== STATISTICAL SUMMARY ==========")
    print(df.describe().T)


    # Extended Statistical Investigation

    numeric_features = df.select_dtypes(
        include="number"
    ).columns.drop(
        ["Run", "Lumi", "Event"],
        errors="ignore"
    )

    print("\n========== SKEWNESS ==========")

    print(
        df[numeric_features]
        .skew()
        .sort_values(ascending=False)
    )

    print("\n========== ZERO VALUES ==========")

    print(
        (df[numeric_features] == 0)
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== NEGATIVE VALUES ==========")

    print(
        (df[numeric_features] < 0)
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== ADDITIONAL QUANTILES ==========")

    print(
        df[numeric_features].quantile(
            [0.01, 0.05, 0.95, 0.99]
        ).T
    )

    plot_feature_kde(df, "Px1")
    plot_feature_kde(df, "Py1")

    compare_kde_bandwidths(df, "Px1")
    compare_kde_bandwidths(df, "Py1")