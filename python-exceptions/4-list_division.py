#!/usr/bin/python3

# asdas = [2, 5, 3, 7, 8, "Dogmeat", 76]
# sasda = [5, 1, "Perro", 234, True, 665]

class WrongType(TypeError):
    pass


class DivisionByZero(ZeroDivisionError):
    pass


class OutOfRange(IndexError):
    pass


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            val1 = None
            val2 = None
            try:
                val1 = my_list_1[i]
            except IndexError:
                raise OutOfRange()

            try:
                val2 = my_list_2[i]
            except IndexError:
                raise OutOfRange()

            if not isinstance(val1, (int, float)) or \
                    not isinstance(val2, (int, float)):
                raise WrongType()

            if val2 == 0:
                raise DivisionByZero()

            division_result = val1 / val2
            result_list.append(division_result)

        except WrongType:
            print("wrong type")
            result_list.append(0)
        except DivisionByZero:
            print("division by 0")
            result_list.append(0)
        except OutOfRange:
            print("out of range")
            result_list.append(0)
        except Exception:
            result_list.append(0)
        finally:
            pass

    return result_list

# list_division(asdas, sasda, 4)
