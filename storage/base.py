from abc import ABC, abstractmethod

class DataStorage(ABC):
    """Абстрактний клас ЗБЕРЕЖЕННЯ_ДАНИХ."""
    @abstractmethod
    def save(self, students_data, filename: str) -> str:
        """Зберігає дані студентів у файл."""
        pass
