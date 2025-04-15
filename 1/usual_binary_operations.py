from bin_constants import BIN_LENGTH
from conversion import decimal_to_binary


def subtract_in_usual_binary(number1: str, number2: str) -> str:
    max_length = max(len(number1), len(number2))
    binary1 = number1.zfill(max_length)
    binary2 = number2.zfill(max_length)
    extra = 0
    result = []

    for i in range(max_length - 1, -1, -1):
        binary1_bit = int(binary1[i]) - extra
        binary2_bit = int(binary2[i])
        if binary1_bit < binary2_bit:
            extra = 1
            binary1_bit += 2
        else:
            extra = 0
        result.append(str(binary1_bit - binary2_bit))
    return ''.join(result[::-1]).lstrip('0')


def binary_multiply(number1: int, number2: int):
    binary1 = decimal_to_binary(number1)
    binary2 = decimal_to_binary(number2)
    sign = '1' if binary1[0] != binary2[0] else '0'
    binary1 = binary1[1:]
    binary2 = binary2[1:]
    result = [0] * 14

    for i in range(BIN_LENGTH - 2, -1, -1):
        for j in range(BIN_LENGTH - 2, -1, -1):
            mul = int(binary1[i]) * int(binary2[j])
            pos_low = i + j + 1
            pos_high = i + j

            summ = mul + result[pos_low]
            result[pos_low] = summ % 2
            result[pos_high] += summ // 2

    return sign + '0' + ''.join(map(str, result))


def binary_greater_equal(number1: str, number2: str):
    number1 = number1.lstrip('0')
    number2 = number2.lstrip('0')
    if len(number1) > len(number2):
        return True
    elif len(number1) < len(number2):
        return False
    else:
        return number1 >= number2


def binary_greater(number1: str, number2: str):
    number1 = number1.lstrip('0')
    number2 = number2.lstrip('0')
    if len(number1) > len(number2):
        return True
    elif len(number1) < len(number2):
        return False
    else:
        return number1 > number2


def binary_divide(number1: int, number2: int) -> str:
    if number2 == 0:
        raise ValueError

    binary1 = decimal_to_binary(number1)
    binary2 = decimal_to_binary(number2)
    sign = '1' if binary1[0] != binary2[0] else '0'
    dividend = decimal_to_binary(abs(number1)).lstrip('0')
    divisor = decimal_to_binary(abs(number2)).lstrip('0')

    quotient1 = quotient2 = remainder = ''
    precision = 5

    for bit in dividend:
        remainder += bit
        if binary_greater_equal(remainder, divisor):
            quotient1 += '1'
            remainder = subtract_in_usual_binary(remainder, divisor)
        else:
            quotient1 += '0'
    if remainder != '0':
        quotient2 = '.'
        for _ in range(precision):
            remainder += '0'
            if binary_greater_equal(remainder, divisor):
                quotient2 += '1'
                remainder = subtract_in_usual_binary(remainder, divisor)
            else:
                quotient2 += '0'

    return sign + (quotient1.zfill(BIN_LENGTH - 1) + quotient2)


def summarize_any_length_binary(number1: str, number2: str):
    max_length = max(len(number1), len(number2)) + 2
    number1 = number1.zfill(max_length)
    number2 = number2.zfill(max_length)
    binlist1 = list(number1)
    binlist2 = list(number2)
    binresult = []
    extra = 0
    for i in range(max_length - 1, -1, -1):
        subtotal = int(binlist1[i]) + int(binlist2[i]) + extra
        binresult.append(str(subtotal % 2))
        extra = subtotal // 2
    return ''.join(binresult)[::-1].lstrip('0')
