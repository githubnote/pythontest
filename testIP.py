import os
import sys


def test_ip():

    print("input IP:")
    IP = input()
    os.system("ping %s" % IP)
    print("\n")

    print("again input 'y/n'")


    if input() == "y":
        test_ip()
    else:
       pass


if __name__ == "__main__":
    test_ip()
