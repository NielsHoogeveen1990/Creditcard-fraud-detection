# Imputer for missing values with non-normal distribution

- fancyimpute: KNN or IterativeImputer
https://pypi.org/project/fancyimpute/


# Encoders for categorical features with high cardinality
- Feature Hashing: https://contrib.scikit-learn.org/categorical-encoding/#


# Sequence of numerical transformers
1. Drop correlated features
2. Drop categorical features with custom chi-square dropper
2. Imputing
3. Encoding:  one-hot / hashing / target encoding / catboost
3. Scaling --> with outliers use RobustScaler or QuantileTransformer
and not StandardScaler. For gradient descent / distance based models, 
scale ALL features (including encoded ones)
 --> gridsearch over different scalers and whether to scale encoded features

