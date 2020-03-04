# Algorithms to use:

1. DBScan Clustering
2. K means
3. Isolation forest
4. Local outlier factor
5. One class SVM


### 1: DBScan 
A density-based anomaly detection method.


### 3: Isolation forest
This algorithm works great with very high dimensional datasets



# Steps
1. EDA
2. Log transform skewed distributions??
2. Standardize data
3. Create PCA
4. Visualize with PCA
5. Evaluate with PR curve AUC


# Definitions
- An outlier is an observation with at least one variable having an unusual value.
- A univariate outlier is an observation with a variable that has an unusual value.
- A multivariate outlier is an observation with at least two variables having unusual values.


Questions:
- Difference between supervised imbalanced set and anomaly detection (novelty)?
- Hoe kun je een import als argument gebruiken? Hoe kun je dus isolationforest.py gebruiken als argument?

Imbalanced learning problems often stump those new to dealing with them. When the ratio between classes in your data is 1:100 or larger, early attempts to model the problem are rewarded with very high accuracy but very low specificity. You can solve the specificity problem in imbalanced learning in a few different ways:
* You can naively weight the classes, making your model preferential to the minority class.
* You can use under-sampling, oversampling or a combination of the two.
* You can switch your goal from trying to balance the dataset, to trying to predict the minority class using outlier detection techniques.


Articles:
- https://towardsdatascience.com/outlier-detection-with-one-class-svms-5403a1a1878c
- https://lambda.grofers.com/anomaly-detection-using-isolation-forest-80b3a3d1a9d8
- https://medium.com/learningdatascience/anomaly-detection-techniques-in-python-50f650c75aaf