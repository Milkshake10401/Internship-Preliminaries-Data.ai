# 1. outlier detection methods and implementation.

### Q1: What are the outlier detection methods that are most commonly used? 

→ **Z-Score or Standard Deviation Method:** This method involves calculating the z-score for each data point and considering values that are beyond a certain threshold as outliers.


→ **Modified Z-Score Method:** Similar to the standard deviation method, this approach uses the modified z-score, which is more robust against outliers.


→ **Percentile Method:** In this method, outliers are detected based on their position in the distribution. Values that fall outside a specified percentile range are considered outliers.


→ **Interquartile Range (IQR) Method:** The IQR method utilizes the range between the first quartile (25th percentile) and the third quartile (75th percentile) of the data. Values outside a certain multiple of the IQR are identified as outliers.


→ **Distance-based Methods:** Techniques like k-nearest neighbors (k-NN) or local outlier factor (LOF) use distance measurements to identify outliers. Data points that have a significantly different distance from their neighbors are labeled as outliers.

### Q2: How do we use pyspark to detect outliers? (For example, a significant increase or decrease)

→ To detect outliers using PySpark, we can leverage the built-in functionality of the PySpark library, specifically the DataFrame API and the MLlib module. Below is a general rule of thumb when using Pyspark: 

(a) Load the data into a PySpark DataFrame.

(b) Preprocess and prepare the data as needed (e.g., handle missing values, convert categorical variables).

(c) Apply feature engineering techniques if required (e.g, Imputation, Logarithmic or Power Transformations, Binning or Discretization, Scaling and Normalization, Interaction Features, One-Hot Encoding, Feature Selection, etc).

(d) Choose an appropriate outlier detection method from the ones mentioned above.

(e) Implement the selected outlier detection method using PySpark transformations and actions.

(f) Depending on the method, you may need to compute statistics, calculate distances, or define thresholds.

(g) Use PySpark's DataFrame operations to identify and flag the outliers.

(h) Perform any additional steps based on your requirements, such as filtering or aggregating the results.

(i) Analyze and interpret the outlier detection results.
