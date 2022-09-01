"""
*Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
input AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
output 6A1F2D7C1A17E
"""

def compress(some_string: str) -> str:
    counter = 1
    result = ""
    for i in range(1, len(my_string)):
        prev = my_string[i - 1]
        curr = my_string[i]

        if prev == curr:
            counter += 1
        elif prev != curr:
            result += f'{counter}{prev}'
            counter = 1

    result += f'{counter}{curr}'
    return result


def decompress(some_string: str) -> str:
    result = ""
    num = ""

    for c in some_string:
        if '0' <= c <= '9':
            num += c
        else:
            result += c * int(num)
            num = ""
    
    return result



if __name__ == "__main__":
    my_string  = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEEZ"
    print(my_string)
    squeezed = compress(my_string)
    print(squeezed)
    expanded = decompress(squeezed)
    print(expanded)
