# Packages
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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
        self._lr = LinearRegression()
        self._df = None
        self._X_train = None
        self._X_test = None
        self._y_train = None
        self._y_test = None
        self._predictions = None

    def read_csv(self) -> None:
        """Read dataset file and assigns dataframe object to _df"""

        self._df = pd.read_csv(self._dataset_file)

    def train_test_split(self) -> None:
        """Splits the dataset in to training set and testing set"""

        X = self._df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                      'Avg. Area Number of Bedrooms', 'Area Population']]
        y = self._df['Price']

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
            'id': 'model1',
            'name': 'Housing Price Prediction',
            'metrics': {
                    'mean_squared_error': mean_squared_error(self._y_test, self._predictions),
                    'mean_absolute_error': mean_absolute_error(self._y_test, self._predictions),
                    'r2_score': r2_score(self._y_test, self._predictions)
            }
        }

        self._db.add_model(model)


def main():
    model = Model(os.path.dirname(__file__) +
                  '/USA_Housing_Data.csv', LocalDatabase())
    model.read_csv()
    model.train_test_split()
    model.train()
    model.test()
    model.add_metrics_to_db()
