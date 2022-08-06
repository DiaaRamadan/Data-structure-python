def is_palindrome(str_input):
    if len(str_input) == 0:
        return True
    if str_input[0] != str_input[len(str_input) - 1]:
        return False
    str_input = str_input[1: None]
    str_input = str_input[:-1]
    is_palindrome(str_input)
    return True


x = "abba"
print(is_palindrome(x))
