import csv, os
from .base import DataStorage

class CSVStorage(DataStorage):
    """Зберігання даних у форматі CSV."""
    def save(self, students_data, filename: str) -> str:
        if not filename.endswith(".csv"):
            filename += ".csv"
        keys = students_data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(students_data)
        return os.path.abspath(filename)
