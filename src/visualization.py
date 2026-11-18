import matplotlib.pyplot as plt

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

    plt.boxplot(df["MR"], vert=False)

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

    plt.boxplot(df["Rsq"], vert=False)

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


if __name__ == "__main__":

    from src.data_loader import load_data

    df = load_data()

    plot_mr_distribution(df)

    plot_mr_boxplot(df)

    plot_rsq_distribution(df)

    plot_rsq_boxplot(df)
    