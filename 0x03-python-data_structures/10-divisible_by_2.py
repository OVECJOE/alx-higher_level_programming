#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_table = []
    for i in my_list:
        truth_table.append(not i % 2)
    return truth_table
