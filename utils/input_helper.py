from ..models.student import Student
from ..models.performance import Performance, DesiredPerformance
from ..models.student_data import StudentData

def prompt_student_input() -> StudentData:
    """Інтерактивне введення даних студента та його успішності."""
    print("Введення даних студента:")
    last = input("Прізвище: ")
    first = input("Ім’я: ")
    patr = input("По батькові: ")
    group = input("Група: ")

    student = Student(last, first, patr, group)

    subjects = input("Предмети (через кому): ").split(",")
    scores = list(map(float, input("Оцінки (через кому): ").split(",")))

    RealPerformance = type("RealPerformance", (Performance,), {
        "average_score": lambda self: sum(self._scores) / len(self._scores)
    })

    real_perf = RealPerformance(subjects, scores)

    desired_scores = list(map(float, input("Бажані оцінки (через кому): ").split(",")))
    desired_perf = DesiredPerformance(subjects, desired_scores)

    return StudentData(student, real_perf, desired_perf)
