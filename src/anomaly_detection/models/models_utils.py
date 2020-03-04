from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from anomaly_detection.preprocessing import get_df
from anomaly_detection.models import isolationforest
import pickle


def split_data(df):
    X = df.drop(columns='Class')
    y = df['Class']

    return train_test_split(X, y, random_state=42)


def fit(model, X_train):
    model = model.pipeline()
    # Train only on X_train, since anomaly detection methods are unsupervised
    model.fit(X_train)

    return model


def evaluate(y_hat, y_true):
    print(classification_report(y_true, y_hat))


def run(datapath, model_version):
    df = get_df(datapath)

    X_train, X_test, y_train, y_test = split_data(df)

    fitted_model = fit(isolationforest, X_train)

    y_hat = fitted_model.predict(X_test)

    evaluate(y_hat, y_test)

    with open(f'src/anomaly_detection/trained_models/model_{model_version}.pkl', 'wb') as file:
        pickle.dump(fitted_model, file)