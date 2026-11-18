import matplotlib.pyplot as plt

def plot_mr_distribution(df):

    plt.figure(figsize=(10, 6))

    plt.hist(df["MR"], bins=50)

    plt.xlabel("MR")
    plt.ylabel("Frequency")
    plt.title("Distribution of MR")

    plt.savefig("results/figures/mr_distribution.png",
            dpi=300, bbox_inches="tight")

    plt.show()



def plot_mr_boxplot(df):

    plt.figure(figsize=(10, 5))

    plt.boxplot(df["MR"], vert=False)

    plt.xlabel("MR")
    plt.title("Boxplot of MR")

    plt.savefig(
        "results/figures/mr_boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


if __name__ == "__main__":

    from src.data_loader import load_data

    df = load_data()

    plot_mr_distribution(df)

    plot_mr_boxplot(df)


q1 = df["MR"].quantile(0.25)
q3 = df["MR"].quantile(0.75)

iqr = q3 - q1

upper_fence = q3 + 1.5 * iqr

potential_outliers = df[df["MR"] > upper_fence]

print("Upper Fence:", upper_fence)
print("Potential Outliers:", len(potential_outliers))
print("Percentage:", len(potential_outliers) / len(df) * 100)    