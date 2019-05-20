#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    li = []
    for i in range(0, list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            res = x / y
            li.append(res)
        except TypeError:
            print("wrong type")
            li.append(0)
        except ZeroDivisionError:
            print("division by 0")
            li.append(0)
        except IndexError:
            print("out of range")
            li.append(0)
        finally:
            pass
    return li
