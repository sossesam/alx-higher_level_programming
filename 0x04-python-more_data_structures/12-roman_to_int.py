#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_list = list(roman_string)
    roman_length = len(roman_list)
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'v': 10,
                  'V': 5, 'I': 1}
    result = 0
    count = 0
    while count < roman_length:
        if roman_list[count] not in roman_dict.keys():
            result = None
            break
        else:
            v = roman_dict[roman_list[count]]
            x = x

            if (v > x) and (count == 1):
                result = v - (result)
                count += 1
            elif (v > x):
                result = v - (result * 2)
                count += 1
            else:
                result += v
                count += 1
    return result
