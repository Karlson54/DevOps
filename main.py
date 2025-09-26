from csv_to_json_converter import CsvToJsonConverter
from json_reader import JsonReader
from student_finder import StudentFinder

if __name__ == "__main__":
    csv_url = "https://informer.com.ua/dut/python/import/st_gt.csv"
    json_path = "students_data.json"

    converter = CsvToJsonConverter()
    converter.read_and_convert(csv_url, json_path)

    json_reader = JsonReader()

    finder = StudentFinder(json_reader)
    finder.load_data(json_path)
    surname_to_find = "Барченко"
    found_students = finder.find_students_by_surname(surname_to_find)
    finder.display_students_info(found_students)
