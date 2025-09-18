from strings_utils import print_string, analyze_string, uppercase_list
from generator_utils import even_odd_generator


if __name__ == "__main__":
    # Демонстрація функцій
    print_string("Hello World")
    analyze_string("HELLO")
    analyze_string("hello")
    analyze_string("HelloWorld")

    print(uppercase_list())

    # Генератор
    gen = even_odd_generator()
    for _ in range(4):
        print(next(gen))
