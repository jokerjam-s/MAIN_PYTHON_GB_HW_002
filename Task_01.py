# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

# В ходе работы пользователю необходимо ввести несколько целых чисел.
# Ввод осуществляется до ввода отрицательного значения.
# На основе введенных чисел формируется список, значения из которого
# в последствии конвертируются из 10-й в 16-ю систему счисления.

BASE_HEX = 16  # основание системы счисления в которую переводим
BASE_DEC = 10  # основание системы счисления из которой переводим
ASCII_START = 55  # стартовый код для отображения (A-F)


def main():
    number: int
    numbers = []

    print('Введите числа для перевода в HEX.\n'
          'Отрицательное число - завершить ввод')
    while True:
        number = get_int('Введите число: ')
        if number < 0:
            break
        numbers.append(number)

    print(' число | моя функция | heh() ')
    print('-----------------------------')
    for i in numbers:
        print(f" {i:<5} | {dec_to_heh(i):11} | {hex(i)}")


# перевод числа в 16-ричное представление
def dec_to_heh(dec_num: int) -> str:
    hex_num: str = ""

    while dec_num:
        div_mod = dec_num % BASE_HEX
        hex_num = (chr(div_mod + ASCII_START) if div_mod >= BASE_DEC else str(div_mod)) + hex_num
        dec_num //= BASE_HEX

    return '0x' + (hex_num if hex_num else "0")


# Запрос численной величины
def get_int(message: str = None) -> int:
    if message is None:
        message = "Введите целое число: "

    return int(input(message))


# Старт
if __name__ == "__main__":
    main()
