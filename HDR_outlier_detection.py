import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession


def main():
    # Reading the csv file
    df = pd.read_csv('Hospitalization_Discharge_Rates.csv')
    n = len(df.columns)
    return 0


if __name__ == '__main__':
    main()
