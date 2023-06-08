#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for index in range(list_length):
        try:
            division = (my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0

        except IndexError:
            print("out of range")
            division = 0

        finally:
            result.append(division)

    return result
