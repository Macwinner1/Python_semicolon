def add_to_list(list_colors, color):
    list_colors.append(color)
    return(list_colors)

def access_third_element(list_numbers):
    for access_third_element in list_numbers:
        if access_third_element == list_numbers[2]:
            return (access_third_element)

def remove_third_element(list_numbers):
    for access_third_element in list_numbers:
        if access_third_element == list_numbers[2]:
            list_numbers.remove(list_numbers[2])
            return (list_numbers)

def list_length_of_string(list_of_strings):
    string_length = []
    for access_element in list_of_strings:
        string_length.append(len(access_element))

    return (string_length)

def ascending_list(list_numbers):
    sort_list_ascending = sorted(list_numbers)
    return(sort_list_ascending)

def even_numbers(list_numbers):
    even_list = []
    for number in list_numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def combine_two_list(list_a, list_b):
    combined_list = list_a + list_b
    return(combined_list)

def more_than_three(list_strings):
    word_list = []
    for word in list_strings:
        if len(word) > 3:
            word_list.append(word)
    return word_list