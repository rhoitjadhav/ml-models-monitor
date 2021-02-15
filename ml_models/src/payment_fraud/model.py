# Packages
import os
import pandas as pd
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

# Modules
from src.models.local_database import LocalDatabase


class Model:
    def __init__(self, dataset_file: str, db: object) -> None:
        """
        Args:
            dataset_file: path to dataset file
            db: database interface object
        """
        self._dataset_file = dataset_file
        self._db = db
        self._lr = LogisticRegression()
        self._df = None
        self._X_train = None
        self._X_test = None
        self._y_train = None
        self._y_test = None
        self._predictions = None

    def read_csv(self):
        """Read dataset file and assigns dataframe object to _df"""

        self._df = pd.read_csv(self._dataset_file)

    def train_test_split(self):
        """Splits the dataset in to training set and testing set"""

        X = self._df[['accountAgeDays', 'numItems',
                      'localTime', 'paymentMethodAgeDays']]
        y = self._df['label']

        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(
            X, y, test_size=0.4, random_state=42)

    def train(self) -> None:
        """Trains model"""
        self._lr.fit(self._X_train, self._y_train)

    def test(self) -> None:
        """Predict results by passing testing set"""
        self._predictions = self._lr.predict(self._X_test)

    def add_metrics_to_db(self) -> None:
        """Add performance metrics to database"""

        model = {
            'id': 'model2',
            'name': 'Payment Fraud Detection',
            'metrics': {
                    'accuracy_score': accuracy_score(self._y_test, self._predictions),
                    'confusion_matrix': confusion_matrix(self._y_test, self._predictions).tolist(),
                    'log_loss': log_loss(self._y_test, self._predictions),
                    'precision_score': precision_score(self._y_test, self._predictions),
                    'recall_score': recall_score(self._y_test, self._predictions),
            }
        }

        self._db.add_model(model)


def main():
    model = Model(os.path.dirname(__file__) +
                  '/Payment_Fraud_Data.csv', LocalDatabase())
    model.read_csv()
    model.train_test_split()
    model.train()
    model.test()
    model.add_metrics_to_db()
