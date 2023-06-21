def merge(first_part, second_part):
    result = []
    index_first = 0
    index_second = 0
    while index_first < len(first_part) and index_second < len(second_part):
        if first_part[index_first] < second_part[index_second]:
            result.append(first_part[index_first])
            index_first += 1
        else:
            result.append(second_part[index_second])
            index_second += 1
# https://www.programiz.com/python-programming/methods/list/extend
    result.extend(first_part[index_first:])
    result.extend(second_part[index_second:])
    return result


def split_list(string):
    if len(string) <= 1:
        return list(string)
    split = len(string) // 2
# https://bobbyhadz.com/blog/python-typeerror-function-object-is-not-subscriptable#:~:text=The%20Python%20%22TypeError%3A%20'function,and%20variables%20don't%20clash.
    first_part = split_list(string[:split])
    second_part = split_list(string[split:])
    return merge(first_part, second_part)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ('', '', False)
    lower_first = first_string.lower()
    lower_second = second_string.lower()
    first_ordered_string = "".join(split_list(lower_first))
    second_ordered_string = "".join(split_list(lower_second))
    if first_ordered_string == second_ordered_string:
        result = True
    if first_ordered_string != second_ordered_string:
        result = False
    # result = first_ordered_string = second_ordered_string
    return (first_ordered_string, second_ordered_string, result)
