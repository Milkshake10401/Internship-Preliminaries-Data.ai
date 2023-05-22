from pyspark.sql import SparkSession


def show_dataframe(df):
    df.show()


def count_dataframe(df):
    return df.count()


def get_dataframe_length(df):
    return len(df.columns)


def print_dataframe_schema(df):
    df.printSchema()


def main():
    # Reading the csv file
    spark = SparkSession.builder.appName("Outlier Detection").getOrCreate()
    df = spark.read.csv("Hospitalization_Discharge_Rates.csv")

    print_dataframe_schema(df)

    return 0


if __name__ == '__main__':
    main()
