from src.util import Util


@Util.singleton
class LocalDatabase:
    def __init__(self):
        self._db_filename = 'db.json'
        self._ml_models_list = Util.read_json(self._db_filename)

    def add_model(self, model):
        model_id = model['id']
        name = model['name']
        metrics = model['metrics']

        self._ml_models_list[model_id] = {
            'name': name,
            'metrics': metrics
        }

        Util.write_to_json(self._db_filename, self._ml_models_list)

    def get_model(self, model_id):
        return self._ml_models_list.get(model_id, False)

    def get_models(self):
        return self._ml_models_list
