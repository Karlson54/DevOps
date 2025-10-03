from abc import ABC, abstractmethod

class Performance(ABC):
    """Абстрактний клас УСПІШНІСТЬ."""
    def __init__(self, subjects, scores):
        if len(subjects) != len(scores):
            raise ValueError("Списки предметів та оцінок повинні збігатися.")
        self._subjects = list(subjects)
        self._scores = [float(s) for s in scores]

    @abstractmethod
    def average_score(self) -> float:
        """Абстрактний метод — повертає середній бал."""
        pass

    def to_dict(self):
        return {
            "subjects": self._subjects,
            "scores": self._scores,
            "average": self.average_score()
        }

class DesiredPerformance(Performance):
    """Клас БАЖАНА_УСПІШНІСТЬ."""
    def __init__(self, subjects, desired_scores, desired_average=None):
        super().__init__(subjects, desired_scores)
        self._desired_average = float(desired_average) if desired_average else None

    def average_score(self) -> float:
        if self._desired_average:
            return self._desired_average
        return sum(self._scores) / len(self._scores) if self._scores else 0.0

    def to_dict(self):
        return {
            "desired_subjects": self._subjects,
            "desired_scores": self._scores,
            "desired_average": self.average_score()
        }
 