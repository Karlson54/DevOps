def print_string(value):
    if not isinstance(value, str):
        print("Error: argument must be a string")
        return
    print(value)


def analyze_string(value):
    if not isinstance(value, str):
        print("Error: argument must be a string")
        return
    if value.isupper():
        print("All letters are uppercase")
    elif value.islower():
        print("All letters are lowercase")
    else:
        print("Mixed case")


def uppercase_list(word="smogtether"):
    return [ch.upper() for ch in word]