def string_to_int(s):
    if len(s) == 0:
        return 0
    return int(s[0]) * 10**(len(s)-1) + string_to_int(s[1:])

input_string = "13531"
result = string_to_int(input_string)
print(result)
