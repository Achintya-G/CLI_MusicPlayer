import json
import os
import sqlite3


# Program Functions
def initialize():
    username = input("\tEnter Your name : \n\t")
    settings = {"name": username}
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    if not os.path.isfile(os.getcwd()+"SongLibrary.db"):
        song_db = sqlite3.connect("SongLibrary.db")
        cur = song_db.cursor()
        cur.execute("CREATE TABLE Tracks(Track_ID INT,Track_Title CHAR,Track_Address CHAR,)")
        cur.execute("CREATE TABLE Albums(Album_ID INT,Album_Name CHAR,)")
        cur.execute("CREATE TABLE Artists(Artist_ID INT,Artist_Name CHAR,)")
        cur.execute("CREATE TABLE Main(Track_ID INT,Artist_ID CHAR,Album_ID INT)")

def greet():
    with open("settings.json","r") as f:
        name = json.load(f)["name"]
    print(f"\t Welcome back {name}")


# User Accessible Functions
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
