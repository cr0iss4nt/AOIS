from bin_constants import MIN_BIN, MAX_BIN
from conversion import decimal_to_binary, decimal_to_binary_ones_complement, decimal_to_binary_twos_complement, \
    binary_twos_complement_to_decimal, binary_to_decimal, ieee754_to_float
from ieee754_operations import summarize_ieee754, float_to_ieee754
from twos_complement_operations import summarize_in_twos_complement, subtract_in_twos_complement
from usual_binary_operations import binary_multiply, binary_divide

while True:
    choice = input("""1) Перевести десятичное число в двоичное (числа от -128 до 127)
2) Сложить два числа в дополнительном коде (от -128 до 127)
3) Вычесть два числа в дополнительном коде (от -128 до 127)
4) Умножить два числа в прямом коде (от -127 до 127)
5) Разделить два числа в прямом коде (от -127 до 127)
6) Сложить два числа в формате IEEE-754 (одинарная точность)
0) Выйти
Ваш выбор: """)
    match choice:
        case '1':
            try:
                number = int(input("Введите целое десятичное число: "))
                if not MIN_BIN <= number <= MAX_BIN:
                    raise ValueError
                if number == MIN_BIN:
                    print("Прямой код: -")
                    print("Обратный код: -")
                else:
                    print("Прямой код:", decimal_to_binary(number))
                    print("Обратный код:", decimal_to_binary_ones_complement(number))
                print("Дополнительный код:", decimal_to_binary_twos_complement(number))
            except:
                print("Неверный ввод!")

        case '2':
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                number1_bin = decimal_to_binary_twos_complement(number1)
                number2_bin = decimal_to_binary_twos_complement(number2)
                result_bin = summarize_in_twos_complement(number1, number2)
                result = binary_twos_complement_to_decimal(result_bin)
                print(f"{number1_bin} + {number2_bin} = {result_bin}")
                print(f"{number1} + {'(' if number2 < 0 else ''}{number2}{')' if number2 < 0 else ''} = {result}")
            except:
                print("Неверный ввод!")

        case '3':
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                result_bin = subtract_in_twos_complement(number1, number2)
                result = binary_twos_complement_to_decimal(result_bin)
                number1_bin = decimal_to_binary_twos_complement(number1)
                number2_bin = decimal_to_binary_twos_complement(number2)
                print(f"{number1_bin} - {number2_bin} = {result_bin}")
                print(f"{number1} - {'(' if number2 < 0 else ''}{number2}{')' if number2 < 0 else ''} = {result}")
            except:
                print("Неверный ввод!")

        case '4':
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                result_bin = binary_multiply(number1, number2)
                result = binary_to_decimal(result_bin)
                number1_bin = decimal_to_binary(number1)
                number2_bin = decimal_to_binary(number2)
                print(f"{number1_bin} * {number2_bin} = {result_bin}")
                print(f"{number1} * {'(' if number2 < 0 else ''}{number2}{')' if number2 < 0 else ''} = {result}")
            except:
                print("Неверный ввод!")

        case '5':
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                result_bin = binary_divide(number1, number2)
                result = binary_to_decimal(result_bin)
                number1_bin = decimal_to_binary(number1)
                number2_bin = decimal_to_binary(number2)
                print(f"{number1_bin} / {number2_bin} = {result_bin}")
                print(f"{number1} / {'(' if number2 < 0 else ''}{number2}{')' if number2 < 0 else ''} = {result}")
            except:
                print("Неверный ввод!")

        case '6':
            try:
                number1 = float(input("Введите первое число: "))
                number2 = float(input("Введите второе число: "))
                result_bin = summarize_ieee754(number1, number2)
                result = ieee754_to_float(result_bin)
                number1_bin = float_to_ieee754(number1)
                number2_bin = float_to_ieee754(number2)
                print(f"{number1_bin} + {number2_bin} = {result_bin}")
                print(f"{number1} + {'(' if number2 < 0 else ''}{number2}{')' if number2 < 0 else ''} = {result}")
            except:
                print("Неверный ввод!")

        case '0':
            print("До свидания!")
            break

        case _:
            print("Неверный ввод!")

    print('')
