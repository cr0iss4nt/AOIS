from bin_constants import MAX_BIN, BIN_LENGTH, BIN_NEGATIVE_128, MIN_BIN, IEEE754_0, IEEE754_MANTISSA_LENGTH, \
    IEEE754_NUMBER_LENGTH, IEEE754_EXP_LENGTH, IEEE754_EXP_BIAS


def binary_to_decimal(number: str):
    result = 0
    sign = -1 if number[0] == '1' else 1
    point_location = number.find('.')
    if point_location == -1:
        for i in range(1, len(number)):
            result += int(number[i]) * 2 ** (len(number) - i - 1)
    else:
        for i in range(1, point_location):
            result += int(number[i]) * 2 ** (point_location - i - 1)
        for i in range(point_location + 1, len(number)):
            result += int(number[i]) * 2 ** (point_location - i)

    return sign * result


def binary_ones_complement_to_decimal(number: str):
    result = 0
    sign = -1 if number[0] == '1' else 1
    if sign == -1:
        number = ''.join(['1' if i == '0' else '0' for i in number])
    for i in range(1, len(number)):
        result += int(number[i]) * 2 ** (len(number) - i - 1)
    return sign * result


def binary_twos_complement_to_decimal(number: str):
    result = binary_ones_complement_to_decimal(number)
    if number[0] == '1':
        result -= 1
    return result


def decimal_to_binary(number: int):
    if abs(number) > MAX_BIN:
        raise ValueError
    sign = str(int(number < 0))
    number = abs(number)
    binary_no_sign = []
    while number > 0:
        binary_no_sign.append(str(number % 2))
        number = number // 2
    return sign + ''.join(binary_no_sign)[::-1].zfill(BIN_LENGTH-1)


def decimal_to_binary_ones_complement(number: int):
    if number >= 0:
        return decimal_to_binary(number)

    positive_binary = decimal_to_binary(-number)
    reverse = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
    return reverse


def decimal_to_binary_twos_complement(number: int):
    if number == MIN_BIN:
        return BIN_NEGATIVE_128
    if number >= 0:
        return decimal_to_binary_ones_complement(number)

    ones_complement = decimal_to_binary_ones_complement(number)

    twos_complement = []
    extra = 1
    for bit in ones_complement[::-1]:
        if bit == '1' and extra == 1:
            twos_complement.insert(0, '0')
        elif bit == '0' and extra == 1:
            twos_complement.insert(0, '1')
            extra = 0
        else:
            twos_complement.insert(0, bit)

    return ''.join(twos_complement).zfill(8)


def float_to_ieee754(number: float) -> str:
    if number == 0:
        return IEEE754_0

    sign = str(int(number < 0))
    number = abs(number)

    order = MAX_BIN
    while number >= 2:
        number /= 2
        order += 1
    while number < 1:
        number *= 2
        order -= 1
    exponent = []
    while order > 0:
        exponent += str(order % 2)
        order //= 2
    while len(exponent) < 8:
        exponent.append('0')
    exponent.reverse()

    mantissa = []
    number -= 1
    for _ in range(IEEE754_MANTISSA_LENGTH):
        number *= 2
        if number >= 1:
            mantissa.append('1')
            number -= 1
        else:
            mantissa.append('0')

    return sign + ''.join(exponent) + ''.join(mantissa)


def ieee754_to_float(number: str) -> float:
    if len(number) != IEEE754_NUMBER_LENGTH:
        raise ValueError
    sign = -1 if number[0] == '1' else 1
    exponent_bin = number[1:IEEE754_EXP_LENGTH+1]
    mantissa_bin = number[IEEE754_EXP_LENGTH+1:]

    exponent = binary_to_decimal('0' + exponent_bin) - IEEE754_EXP_BIAS
    mantissa = binary_to_decimal('01' + mantissa_bin) / pow(2, IEEE754_MANTISSA_LENGTH)
    return sign * pow(2, exponent) * mantissa
