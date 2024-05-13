def echo(*x):
    """Echos anything passed to this function"""
    for i in x[0]:
        print(i, end=" ")
    print()


def cliHelp(x):
    """Pass a function as an argument to see how it must be used"""
    if x != []:
        if x[0] in func_list:
            func = func_list[x[0]]
            print(func.__doc__)
            return
        else:
            print("Invalid argument \n\t\"", x[0], "\" Not a valid function name", sep="")
            return
    print("pass a function as an argument to see how it must be used")


func_list = {"echo": echo,
             "help": cliHelp,}
