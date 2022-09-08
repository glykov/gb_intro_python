def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            for v in data[i].values():
                fout.write(f'{v}\n')

    
def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def read_txt(filename: str) -> list:
    data = []
    fields = ["", "Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        record = {}
        counter = 0
        for line in fin:
            counter += 1
            record[fields[counter]] = line.strip()
            print(counter)
            print(record)
            if counter == 4:
                data.append(record)
                record = {}
                counter = 0        
    return data

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
    return "Такой абонент отсутвует"


def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой абонент отсутвует"

def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)
