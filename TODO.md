# Algorithms to use:

Use a base algorithm: random, for a baseline.

1. DBScan 
2. Elliptic Envelope
2. Isolation forest
3. Local outlier factor
4. One class SVM: unsupervised algo used for novelty detection. 
Hence needs to be trained on a dataset without outliers.


### 1: DBScan 
A density-based anomaly detection method.


### 3: Isolation forest
This algorithm works great with very high dimensional datasets

Partitions are created by randomly selecting a feature and 
then randomly creating a split value between the maximum and 
the minimum value of the feature. We keep on creating the partitions until 
we isolate all the points(in most cases we also set a limit on 
number of partitions/height of the tree).

Isolation forest is an ensemble method. 
So we create multiple Isolation trees(generally 100 trees will suffice) and 
we take the average of all the path lengths.
This average path length will then decide whether a point is anomalous or not.

Note that it is always better to represent score between 0 to 1 because 
the score can now be interpreted as a probability. 
For example, say for a data point if we get the anomaly score as 0.8, 
then we can interpret such that the point has a probability of 80% 
to be an anomalous point.

###### Contamination 
Contamination is the assumption about the fraction of anomalies in the dataset. 
This number is set by the intuition of the domain experts- generally the 
domain experts will have a rough idea about the fraction of 
the anomalies in the dataset. For most real-life cases, a value of 0.1 works.



# Steps
1. EDA
2. Log transform skewed distributions??
2. Standardize data
3. Create PCA
4. Visualize with PCA

Train model with Grid search

5. Evaluate with PR curve AUC

Interpret with SHAP / LIME

6. Fill DB (sqlite) with test data and create IDs for each row
7. Create Flask API that returns true or false for anomalies, by supplying an ID


# Definitions
- An outlier is an observation with at least one variable having an unusual value.
- A univariate outlier is an observation with a variable that has an unusual value.
- A multivariate outlier is an observation with at least two variables having unusual values.

# Why conventional anomaly methods don't work:
- Works well only for near to normal distribution
- Detects only one anomaly per test
- Works well only for a 1-Dimensional data set


Questions:
- Hoe kun je een import als argument gebruiken? Hoe kun je dus isolationforest.py gebruiken als argument?

Imbalanced learning problems often stump those new to dealing with them. When the ratio between classes in your data is 1:100 or larger, early attempts to model the problem are rewarded with very high accuracy but very low specificity. You can solve the specificity problem in imbalanced learning in a few different ways:
* You can naively weight the classes, making your model preferential to the minority class.
* You can use under-sampling, oversampling or a combination of the two.
* You can switch your goal from trying to balance the dataset, to trying to predict the minority class using outlier detection techniques.


Articles:
- https://towardsdatascience.com/outlier-detection-with-one-class-svms-5403a1a1878c
- https://lambda.grofers.com/anomaly-detection-using-isolation-forest-80b3a3d1a9d8
- https://medium.com/learningdatascience/anomaly-detection-techniques-in-python-50f650c75aaf