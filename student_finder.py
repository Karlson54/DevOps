class StudentFinder:
    def __init__(self, json_reader):
        self.json_reader = json_reader
        self.data = None

    def load_data(self, path):
        """Завантаження даних з JSON."""
        self.data = self.json_reader.read_data(path)

    def find_students_by_surname(self, surname):
        """Пошук студентів за прізвищем."""
        if not self.data:
            raise ValueError("Спочатку завантажте дані через load_data.")
        return [student for student in self.data if student['Прізвище'] == surname]

    def display_students_info(self, students):
        """Виведення інформації про знайдених студентів."""
        for student in students:
            pib = f"{student['Прізвище']} {student['Ім\'я']}"
            print(f"ПІБ: {pib}")
            print("Завдання:")
            for key, value in student.items():
                if 'Завдання' in key:
                    print(f"  {key}: {value}")
            print("-----------")
