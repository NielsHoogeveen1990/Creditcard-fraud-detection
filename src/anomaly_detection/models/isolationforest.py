from sklearn.ensemble import IsolationForest

from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def pipeline():
    return make_pipeline(
        SimpleImputer(),
        StandardScaler(),
        IsolationForest(n_estimators=100,
                        max_samples='auto',
                        contamination=0.01,
                        max_features=1.0,
                        bootstrap=False,
                        n_jobs=-1,
                        random_state=42,
                        verbose=0,
                        behaviour="new")
    )


