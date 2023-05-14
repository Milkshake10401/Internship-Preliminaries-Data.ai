import pandas as pd


def main():
    # Reading the csv file
    df = pd.read_csv('Hospitalization_Discharge_Rates.csv')
    n = len(df.columns)
    return 0


if __name__ == '__main__':
    main()
