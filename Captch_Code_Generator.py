import random
from colorama import Fore, init


def ranpass():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "!@#$%&*_."

    string = lower + upper + number + symbols
    length = 12

    password = "".join(random.sample(string, length))
    result = (Fore.RED + "Your password is : ")
    



    print("")
    print(result + password)
    print("")


ranpass()