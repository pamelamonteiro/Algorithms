def is_palindrome_iterative(word):
    if word == '':
        return False
    txt = word[::-1]
    index = 0
    array_size = len(word) - 1
    while index <= array_size:
        if word[index] != txt[index]:
            return False
        index += 1
    return True

# https://www.w3schools.com/python/python_howto_reverse_string.asp
# https://www.freecodecamp.org/news/typeerror-string-indices-must-be-integers-how-to-fix-in-python/
