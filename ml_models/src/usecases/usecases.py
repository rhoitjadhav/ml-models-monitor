class Usecases:
    def __init__(self, db):
        self._db = db

    def get_all_models(self) -> dict:
        """
        Get all models details

        Returns:
            dict: List of models details data
        """
        try:
            models = self._db.get_models()
            if models == {}:
                result = {
                    'success': True, 'message': 'No models found in database', 'data': models}
            else:
                result = {'success': True,
                          'message': 'Data Found', 'data': models}

            return result

        except Exception as e:
            return {'success': False, 'message': f'Error while getting models details: {e}'}

    def get_performance_metrics(self, model_id: str) -> dict:
        """ 
        Get model performance metrics
        Args:
            model_id: model id

        Returns:
            dict: Performance Metrics data of model
        """
        try:
            model = self._db.get_model(model_id)
            if model:
                result = {'success': True, 'message': 'Data Found',
                          'data': model['metrics']}
            else:
                result = {'success': False, 'message': 'Model not found in db'}

            return result

        except Exception as e:
            return {'success': False, 'message': f'Error while getting performance metrics for {model_id}: {e}'}
