import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin


class CorrectTypesTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        types = {
            column: "category" for column in X.columns if X[column].dtype == "object"
        }
        return X.astype(types)


class ExtremeOutlierCleaningTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        numerical = X.select_dtypes(include="number").columns

        for column in numerical:
            q1 = X[column].quantile(0.25)
            q3 = X[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 3 * iqr
            upper_bound = q3 + 3 * iqr
            X = X.loc[(X[column] > lower_bound) & (X[column] < upper_bound)]

        return X


class PretrainedMinMaxScaler(BaseEstimator, TransformerMixin):
    def __init__(self, scaler):
        self.scaler = scaler

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return self.scaler.transform(X)


class PretrainedLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, encoder):
        self.encoder = encoder

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return self.encoder.inverse_transform(X)


class DummyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None, drop_first=False, dtype=int):
        self.columns = columns
        self.drop_first = drop_first
        self.dtype = dtype

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if self.columns is None:
            categorical_cols = X.select_dtypes(include="category").columns
        else:
            categorical_cols = self.columns

        X = pd.get_dummies(
            X, columns=categorical_cols, drop_first=self.drop_first, dtype=self.dtype
        )
        return X


class NumericalImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy="mean"):
        self.strategy = strategy
        self.imputer = SimpleImputer(strategy=self.strategy)

    def fit(self, X, y=None):
        self.imputer.fit(X[["stem-height", "stem-width"]])
        return self

    def transform(self, X):
        X[["stem-height", "stem-width"]] = self.imputer.transform(
            X[["stem-height", "stem-width"]]
        )
        return X


class CategoricalImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy="most_frequent"):
        self.strategy = strategy
        self.imputer = SimpleImputer(strategy=self.strategy)

    def fit(self, X, y=None):
        self.imputer.fit(X[X.select_dtypes(include="category").columns])
        return self

    def transform(self, X):
        X[X.select_dtypes(include="category").columns] = self.imputer.transform(
            X[X.select_dtypes(include="category").columns]
        )
        return X
