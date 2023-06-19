from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.sql.functions import col


def show_dataframe(df):
    df.show()


def count_dataframe(df):
    return df.count()


def get_dataframe_length(df):
    return len(df.columns)


def print_dataframe_schema(df):
    df.printSchema()


def select_relevant_features(df):
    feature_columns = df.columns[1:]  # Assuming the first column is an identifier
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    feature_vector = assembler.transform(df)
    return feature_vector


def scale_features(feature_vector):
    scaler = StandardScaler(inputCol="features", outputCol="scaled_features")
    scaler_model = scaler.fit(feature_vector)
    scaled_data = scaler_model.transform(feature_vector)
    return scaled_data


def detect_outliers(scaled_data):
    kmeans = KMeans(k=5, seed=1)
    model = kmeans.fit(scaled_data.select("scaled_features"))
    predictions = model.transform(scaled_data)
    threshold = predictions.agg({"distance_to_center": "mean"}).first()[0]
    outliers = predictions.filter(col("distance_to_center") > threshold)
    return outliers


def main():
    # Reading the csv file
    spark = SparkSession.builder.appName("Outlier Detection").getOrCreate()
    df = spark.read.csv("Hospitalization_Discharge_Rates.csv")

    print_dataframe_schema(df)

    feature_vector = select_relevant_features(df)
    scaled_data = scale_features(feature_vector)
    outliers = detect_outliers(scaled_data)

    show_dataframe(outliers)
    print("Number of outliers:", count_dataframe(outliers))
    print("Number of features:", get_dataframe_length(outliers))

    return 0


if __name__ == '__main__':
    main()
