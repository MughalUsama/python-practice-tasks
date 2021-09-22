import sys


class MyString:

    def __init__(self, string_val=""):
        self.__my_string = string_val

    def getString(self):
        return self.__my_string

    def printString(self):
        print(self.__my_string)

    def clear(self):
        self.__my_string = ""

    def length(self):
        return len(self.__my_string)

    def reverse(self):
        self.__my_string = self.__my_string[::-1]


def test_my_string(a_str):
    an_instance = MyString(a_str)
    print("String Length : ", end="")
    print(an_instance.length())
    print("String Value : ", end="")
    an_instance.printString()
    an_instance.reverse()
    print("--String Reversed--")
    print("String Value : ", end="")
    an_instance.printString()
    print("String Cleared.")
    an_instance.clear()
    print("String Value : ", end="")
    an_instance.printString()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        test_my_string("A sample String")
    else:
        test_my_string(sys.argv[1])
