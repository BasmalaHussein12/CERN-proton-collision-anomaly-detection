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



if __name__ == "__main__":

    from src.data_loader import load_data

    df = load_data()

    plot_mr_distribution(df)