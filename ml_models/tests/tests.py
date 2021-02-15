import unittest
from src.usecases.usecases import Usecases
from src.housing_price import model as model1
from src.payment_fraud import model as model2
from src.models.local_database import LocalDatabase


class Tests(unittest.TestCase):
    _usecase = Usecases(LocalDatabase())
    _model1 = model1
    _model2 = model2

    def setUp(self):
        self._model1.main()
        self._model2.main()

    def test_1(self):
        """Get All Models List"""
        result = self._usecase.get_all_models()
        self.assertEqual(result['success'], True)

    def test_2(self):
        """Get Model Performance Metrics"""
        tests = [
            ('model1', True),
            ('model2', True),
            ('model3', False)
        ]

        for test in tests:
            result = self._usecase.get_performance_metrics(test[0])
            self.assertEqual(result['success'], test[1])
