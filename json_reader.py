import json
from data_reader import DataReader

class JsonReader(DataReader):
    def read_data(self, path):
        """Читання даних з JSON файлу."""
        with open(path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def display_data(self, path):
        """Вивести всі дані з JSON."""
        data = self.read_data(path)
        print("Дані з JSON:")
        for row in data:
            print(row)
