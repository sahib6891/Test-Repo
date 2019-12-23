import sys
import requests


# print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


if __name__ == "__main__":
    print(greet("Sahib"))

