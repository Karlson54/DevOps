def filename_from_student(student, work_number: int, fmt: str, multiple: bool = False) -> str:
    """Формування імені файлу за шаблоном: Прізвище_Ім’я_ПоБатькові_Група_PRN.формат"""
    base = f"{student.last_name}_{student.first_name}_{student.patronymic}_{student.group_number}"
    if multiple:
        base += "_декілька"
    base += f"_PR{work_number}"
    return f"{base}.{fmt.lower()}"
