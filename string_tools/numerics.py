"""
Functions for expressing numbers as strings
"""

#
# adds zeros left of the decimal point (in a string representation of a number), to facilitate string sorting
# of texts with numerical identifiers
#
def left_pad_zeros_for_a_number(number, number_of_digits_left_of_the_decimal_point):
    number_as_char_list = [c for c in str(number)]
    number_of_characters_to_add = number_of_digits_left_of_the_decimal_point - len(number_as_char_list)
    new_list = []
    if number_of_characters_to_add >= 1:
        new_list.extend(['0'] * number_of_characters_to_add)
    new_list.extend(number_as_char_list)
    return ''.join(new_list)

#
# make an integer an adjective (sort of)
#
def make_integer_an_adjective(int_number):
    number_as_string = str(int_number)
    last_digit = number_as_string[-1]
    if last_digit in ['0', '4', '5', '6', '7', '8', '9'] or number_as_string in ['11', '12', '13']:
        return number_as_string + 'th'
    elif number_as_string[-2:] in ['11', '12', '13']:
        return number_as_string + 'th'
    elif last_digit == '1':
        return number_as_string + 'st'
    elif last_digit == '2':
        return number_as_string + 'nd'
    elif last_digit == '3':
        return number_as_string + 'rd'
    else:
        return number_as_string

#
# shortcut for scientific notation because I can never remember how to actually do it
#
def scientific_notation_shortcut(float_number, significant_digits):
    format_string = '%0.' + str(significant_digits) + 'e'
    return(str(eval(format_string % float_number)))
