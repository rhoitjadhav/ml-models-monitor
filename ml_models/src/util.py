import json


class Util:
    @staticmethod
    def singleton(class_):
        instances = {}

        def get_instance(*args, **kwargs):
            if class_ not in instances:
                instances[class_] = class_(*args, **kwargs)
            return instances[class_]

        return get_instance

    @staticmethod
    def read_json(file):
        with open(file, 'r') as fp:
            return json.load(fp)

    @staticmethod
    def write_to_json(file, data):
        with open(file, 'w') as fp:
            json.dump(data, fp, indent=4)
