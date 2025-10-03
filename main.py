from models.student import Student
from utils.input_helper import prompt_student_input
from utils.filename import filename_from_student
from storage.json_storage import JSONStorage
from storage.xml_storage import XMLStorage
from storage.csv_storage import CSVStorage

def main():
    print("=== Лабораторна робота: Збереження даних студентів ===")
    n = int(input("Скільки студентів ввести? ") or "1")
    students_data = [prompt_student_input().to_dict() for _ in range(n)]

    fmt = input("Формат збереження (json/xml/csv): ").lower() or "json"
    work_number = int(input("Номер роботи: ") or "5")

    first_student_dict = students_data[0]["student"]
    student = Student(first_student_dict["last_name"],
                      first_student_dict["first_name"],
                      first_student_dict["patronymic"],
                      first_student_dict["group_number"])
    filename = filename_from_student(student, work_number, fmt, multiple=n>1)

    if fmt == "json":
        storage = JSONStorage()
    elif fmt == "xml":
        storage = XMLStorage()
    else:
        storage = CSVStorage()

    path = storage.save(students_data, filename)
    print(f"✅ Дані успішно збережено у файл: {path}")

if __name__ == "__main__":
    main()
