def convert_to_mandarin(num_str):
    # Define the translation dictionary for digits 0 to 10
    trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba',
             '9': 'jiu', '10': 'shi'}

    # Convert the input number string into a list of digits
    digits = list(num_str)

    # If the number is between 0 and 10, simply return the translation from the dictionary
    if len(digits) == 1:
        return trans[num_str]

    # If the number is between 11 and 19, handle it as "ten digit"
    if len(digits) == 2 and digits[0] == '1':
        return "shi " + trans[digits[1]]

    # If the number is between 20 and 99, handle it as "digit ten digit"
    if len(digits) == 2 and digits[0] != '1':
        if digits[1] == '0':
            return trans[digits[0]] + " shi"
        else:
            return trans[digits[0]] + " shi " + trans[digits[1]]


# Test cases
print(convert_to_mandarin('36'))  # Output: san shi liu
print(convert_to_mandarin('20'))  # Output: er shi
print(convert_to_mandarin('16'))  # Output: shi liu
print(convert_to_mandarin('25'))

