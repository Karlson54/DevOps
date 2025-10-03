import json, os
from .base import DataStorage

class JSONStorage(DataStorage):
    """Зберігання даних у форматі JSON."""
    def save(self, students_data, filename: str) -> str:
        if not filename.endswith(".json"):
            filename += ".json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(students_data, f, ensure_ascii=False, indent=4)
        return os.path.abspath(filename)
