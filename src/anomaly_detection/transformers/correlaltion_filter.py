from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
import numpy as np

class CorrelationFilter(TransformerMixin, BaseEstimator):

    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def fit(self, X, y=None):
        self.columns_to_drop_ = self.get_columns_to_drop(X, y)
        return self

    def transform(self, X):
        return X.drop(columns=self.columns_to_drop_)

    @staticmethod
    def _get_abs_corr(X):
        return X.corr().abs() - np.eye(X.shape[1])

    def get_columns_to_drop(self, X, y):

        cols_to_drop = []
        abs_corr = self._get_abs_corr(X)

        while abs_corr.max().max() > self.threshold:
            highest_corr_cols = list(abs_corr.unstack().idxmax())
            col_to_drop = self.choose_from_two(X, y, highest_corr_cols)

            cols_to_drop.append(col_to_drop)
            X = X.drop(columns=col_to_drop)
            abs_corr = self._get_abs_corr(X)

        return cols_to_drop

    def choose_from_two(self, X, y, cols):
        # Of the two columns that share the highest correlation, drop the one most to the back
        return cols[-1]


class CorrFilterLowVariance(CorrelationFilter):
    def __init__(self):
        super(CorrFilterLowVariance, self).__init__()

    def choose_from_two(self, X, y, cols):
        # Of the two columns that share the highest correlation, drop the one with lowest variance
        return X.loc[:, cols].var().idxmin()


class CorrFilterLowTargetCorrelation(CorrelationFilter):
    def __init__(self):
        super(CorrFilterLowTargetCorrelation, self).__init__()

    def choose_from_two(self, X, y, cols):
        # Of the two columns that share the highest correlation, drop the one with lowest correlation with y
        return pd.concat([X.loc[:, cols], y], axis=1).corr()[y.name].idxmin()


class CorrFilterHighTotalCorrelation(CorrelationFilter):
    def __init__(self):
        super(CorrFilterHighTotalCorrelation, self).__init__()

    def choose_from_two(self, X, y, cols):
        # Of the two columns that share the highest correlation,
        # drop the one with highest correlation with other columns
        return X.corr().loc[:, cols].sum(axis=0).idxmax()