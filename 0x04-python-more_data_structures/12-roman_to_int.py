#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = roman_numerals.get(roman_string[-1], 0)

    for i in range(len(roman_string) - 2, -1, -1):
        current_numeral = roman_numerals[roman_string[i]]
        next_numeral = roman_numerals[roman_string[i + 1]]

        if current_numeral < next_numeral:
            total -= current_numeral
        else:
            total += current_numeral

    return total
