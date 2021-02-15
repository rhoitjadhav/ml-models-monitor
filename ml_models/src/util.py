import json


class Util:
    @staticmethod
    def singleton(class_: type):
        """
        Makes Single class
        
        Args:
            class_: class
        
        Returns:
            object of class
        """
        instances = {}

        def get_instance(*args, **kwargs):
            if class_ not in instances:
                instances[class_] = class_(*args, **kwargs)
            return instances[class_]

        return get_instance

    @staticmethod
    def read_json(file: str) -> dict:
        """ 
        Reads json file and convert its content to dict format
        
        Args:
            file: path of file
        
        Returns:
            dict: dictionary json file data
        """
        with open(file, 'r') as fp:
            return json.load(fp)

    @staticmethod
    def write_to_json(file: str, data: dict) -> None:
        """
        Writes data to json file
        
        Args:
            file: path of file
            data: dict data to be write
        """
        with open(file, 'w') as fp:
            json.dump(data, fp, indent=4)
