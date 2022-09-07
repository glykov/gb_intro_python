def show_menu() -> int:
    print("\nВыберите необходимое действие: ")
    print("1. Отобразить весь справочник")
    print("2. Найти абонента по фамилии")
    print("3. Найти абонента по номеру телефона")
    print("4. Добавить абонента в справочник")
    print("5. Сохранить справочник в текстовом формате")
    print("6. Закончить работу")
    choice = int(input())
    return choice

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)


def get_search_name() -> str:
    return input("Введите фамилию для поиска: ")


def get_search_number() -> str:
    return input("Введите номер телефона для поиска: ")


def get_new_user() -> str:
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    description = input("Введите описание абонента: ")
    return f'{last_name},{first_name},{phone_number},{description}'

def get_file_name() -> str:
    return input("Введите название файла для сохранения: ")
