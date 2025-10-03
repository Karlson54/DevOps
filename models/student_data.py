class StudentData:
    """Клас ДАНІ_СТУДЕНТА — поєднує Student, Performance та DesiredPerformance."""
    def __init__(self, student, real_perf, desired_perf):
        self.__student = student
        self.__real_perf = real_perf
        self.__desired_perf = desired_perf

    def to_dict(self):
        return {
            "student": self.__student.to_dict(),
            "real_performance": self.__real_perf.to_dict(),
            "desired_performance": self.__desired_perf.to_dict()
        }
