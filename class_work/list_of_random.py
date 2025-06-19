import random

def create_random_numbers(number):
    for count in range(number):
        random_list  = (random.randint(1, 50))
        return random_list

def get_length(random_list):
    length = 0
    for number in random_list:
        length += 1
    return length

def get_sum_of_even_numbers(random_list):
    total = 0
    for index,value in enumerate(random_list):
        if index % 2 != 0:
            total += value
    return total

def get_sum_of_odd_numbers(random_list):
    sum_value = 0
    for index,number in enumerate(random_list):
        if index % 2 == 0:
            sum_value += number
    return sum_value

def get_multiply_of_element_at_every_third_position(random_list):
    sum_value = 1
    for index,number in enumerate(random_list):
        if index % 3 == 0:
            sum_value *= number
    return sum_value

def get_the_average_of_all_elements(random_list):
    out_come = 0
    for number in random_list:
        out_come += number
    return out_come / get_length(random_list)

