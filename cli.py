import os
import json
from cliFuncs import *


def assigner(function):
    print("\t", end="")
    return func_list[function]


if __name__ == "__main__":
    # Checking if program is being run for first time and running initialize function
    if not os.path.isfile(os.getcwd()+"\\settings.json"):
        username = input("\tEnter Your name : \n\t")
        settings = {"name": username}
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)
    else:
        with open("settings.json","r") as f:
            name = json.load(f)["name"]
        print(f"\t Welcome back {name}")

    # running a loop to continuously take input
    while True:
        result = None
        # taking input and removing trailing/leading spaces and making into a list
        n = input(">>> ")
        n = n.strip().split(" ")
        # Checking if first word is a function keyword
        if n[0] in func_list:
            func = assigner(n[0])
            # Checking if additional parameters are being passed onto function
            if n[1:] is not None:
                result = func(n[1:])
            # Checkin if result from function is not null and printing
            if result is not None and result != []:
                print("\t", result)
