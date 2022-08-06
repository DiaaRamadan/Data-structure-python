def reverse_string(str_input):
    if not str_input:
        return " "
    return reverse_string(str_input[slice(1, None)]) + str_input[0]

