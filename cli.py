from cliFuncs import *


def assigner(function):
    print("\t", end="")
    return func_list[function]


if __name__ == "__main__":
    while True:
        result = None
        n = input(">>> ")
        n = n.strip().split(" ")
        if n[0] in func_list:
            func = assigner(n[0])
            if n[1:] is not None:
                result = func(n[1:])
            if result is not None and result != []:
                print("\t", result)
