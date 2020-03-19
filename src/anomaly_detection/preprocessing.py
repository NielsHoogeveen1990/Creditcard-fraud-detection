import pandas as pd
import numpy as np
from anomaly_detection.utils import log_step


def read_data(data_path):
    return pd.read_csv(data_path)


def drop_irrelevant_features(df, *cols):
    try:
        return df.drop(columns=list(cols))
    except:
        return df


def replace_classes(df):
    return df.assign(
        Class = lambda d: d['Class'].replace({0: 1, 1: -1})
    )


@log_step
def get_df(data_path):
    return (read_data(data_path)
    .pipe(drop_irrelevant_features, 'Time')
    .drop_duplicates(keep='first')
    .pipe(replace_classes)
            )