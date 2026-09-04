#!/usr/bin/python3
"""Module that divides two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide my_list_1 by my_list_2 element by element."""
    new_list = []
    for i in range(list_length):
        divide_result = 0
        try:
            divide_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(divide_result)
    return new_list
