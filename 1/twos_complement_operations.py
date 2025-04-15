from bin_constants import BIN_LENGTH
from conversion import decimal_to_binary_twos_complement


def twos_complement_negation(binary_str: str):
    inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary_str)

    negated_value = list(inverted_bits)
    extra = 1

    for i in range(7, -1, -1):
        if extra == 0:
            break
        if negated_value[i] == '1':
            negated_value[i] = '0'
        else:
            negated_value[i] = '1'
            extra = 0

    return ''.join(negated_value)


def summarize_in_twos_complement(number1: int, number2: int):
    binary1 = decimal_to_binary_twos_complement(number1)
    binary2 = decimal_to_binary_twos_complement(number2)
    binlist1 = list(binary1)
    binlist2 = list(binary2)
    binresult = []
    extra = 0
    for i in range(BIN_LENGTH - 1, -1, -1):
        subtotal = int(binlist1[i]) + int(binlist2[i]) + extra
        binresult.insert(0, str(subtotal % 2))
        extra = subtotal // 2
    return ''.join(binresult)


def subtract_in_twos_complement(number1: int, number2: int):
    binary1 = decimal_to_binary_twos_complement(number1)
    binary2 = decimal_to_binary_twos_complement(number2)
    binlist1 = list(binary1)
    binlist2 = list(twos_complement_negation(binary2))
    binresult = []
    extra = 0
    for i in range(BIN_LENGTH - 1, -1, -1):
        subtotal = int(binlist1[i]) + int(binlist2[i]) + extra
        binresult.append(str(subtotal % 2))
        extra = subtotal // 2
    return (''.join(binresult))[::-1]
