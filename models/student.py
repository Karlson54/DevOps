class Student:
    """Клас СТУДЕНТ — усі поля приватні, доступ через властивості."""
    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 group_number: str, birth_date: str = None, address: str = None):
        self.__last_name = last_name.strip()
        self.__first_name = first_name.strip()
        self.__patronymic = patronymic.strip()
        self.__group_number = group_number.strip()
        self.__birth_date = birth_date.strip() if birth_date else None
        self.__address = address.strip() if address else None

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @property
    def group_number(self) -> str:
        return self.__group_number

    @property
    def birth_date(self) -> str:
        return self.__birth_date

    @property
    def address(self) -> str:
        return self.__address

    def full_name(self) -> str:
        return f"{self.__last_name} {self.__first_name} {self.__patronymic}"

    def to_dict(self):
        return {
            "last_name": self.__last_name,
            "first_name": self.__first_name,
            "patronymic": self.__patronymic,
            "group_number": self.__group_number,
            "birth_date": self.__birth_date,
            "address": self.__address
        }
