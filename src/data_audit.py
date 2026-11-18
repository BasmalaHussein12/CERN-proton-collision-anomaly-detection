
from src.data_loader import load_data


def audit_data(df):

    print("Dataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nNumerical Summary:")
    print(df.describe().T)

if __name__ == "__main__":

    df = load_data()

    audit_data(df)
