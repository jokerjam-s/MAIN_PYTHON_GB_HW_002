# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

BASE_DIV = 16  # основание системы счисления
ASCII_START = 55  # стартовый код для отображения (A-F)


def main():
    number: int = get_int()
    print(dec_to_heh(number), hex(number))


# перевод числа в 16-ричное представление
def dec_to_heh(number: int) -> str:
    rest: int = number
    heh_num: str = ""

    while rest:
        div_mod = rest % BASE_DIV
        if div_mod > 9:
            heh_num = chr(div_mod + ASCII_START) + heh_num
        else:
            heh_num = str(div_mod) + heh_num
        rest //= BASE_DIV

    return '0x' + heh_num


# Запрос численной величины
def get_int(message: str = None) -> int:
    if message is None:
        message = "Введите целое число: "

    return int(input(message))


# Старт
if __name__ == "__main__":
    main()
