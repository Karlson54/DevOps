import sys

def main():
    if '--help' in sys.argv:
        print("Використання: python src/sys_tool.py\n"
              "Друкує 'командна строка' лише при прямому запуску.")
    else:
        print("командна строка")

if __name__ == "__main__":
    main()
