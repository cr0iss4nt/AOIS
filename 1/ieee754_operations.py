from bin_constants import IEEE754_0, IEEE754_EXP_LENGTH, IEEE754_MANTISSA_LENGTH
from conversion import binary_to_decimal, float_to_ieee754
from usual_binary_operations import binary_greater_equal, subtract_in_usual_binary, binary_greater, \
    summarize_any_length_binary


def summarize_ieee754(number1, number2):
    if number1 < 0 or number2 < 0:
        raise ValueError
    binary1 = float_to_ieee754(number1)
    binary2 = float_to_ieee754(number2)
    if binary2 == IEEE754_0:
        return binary1
    elif binary1 == IEEE754_0:
        return binary2

    exponent1 = binary1[1:IEEE754_EXP_LENGTH + 1]
    exponent2 = binary2[1:IEEE754_EXP_LENGTH + 1]
    mantissa1 = '1' + binary1[IEEE754_EXP_LENGTH + 1:]
    mantissa2 = '1' + binary2[IEEE754_EXP_LENGTH + 1:]

    if exponent1 == exponent2 and binary_greater_equal(mantissa1, mantissa2):
        max_number = 1
    elif binary_greater(exponent1, exponent2):
        max_number = 1
    else:
        max_number = 2
    max_exponent = exponent1 if max_number == 1 else exponent2
    if max_number == 1:
        shift_bin = subtract_in_usual_binary(exponent1, exponent2)
    else:
        shift_bin = subtract_in_usual_binary(exponent2, exponent1)
    shift = binary_to_decimal(shift_bin.zfill(8))
    if max_number == 1:
        mantissa2 = '0' * shift + mantissa2
        mantissa1 += '0' * shift
    else:
        mantissa1 = '0' * shift + mantissa1
        mantissa2 += '0' * shift
    mantissa_sum = summarize_any_length_binary(mantissa1, mantissa2)
    if len(mantissa_sum) > len(max(mantissa1, mantissa2)):
        max_exponent = summarize_any_length_binary(max_exponent, '1')

    return '0' + max_exponent.rjust(IEEE754_EXP_LENGTH, '0') + mantissa_sum[1:].ljust(IEEE754_MANTISSA_LENGTH, '0')[:IEEE754_MANTISSA_LENGTH]
