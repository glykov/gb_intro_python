"""
Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""

def remove_from_string(where: str, what: str) -> str:
    result = ''
    for word in where.split():
        if what not in word:
            result += word
    return result

if __name__ == "__main__":
    my_str = 'абв текстабв абвтекст теабвкст текст'
    print(remove_from_string(my_str, 'абв'))
    