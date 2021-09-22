import sys


def sum_of_2_numbers(num1, num2):
    return num1+num2


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            print("Please enter 2 Numbers")
        else:
            print(sum_of_2_numbers(float(sys.argv[1]), float(sys.argv[2])))
    except ValueError:
        print("Please enter numbers only.")
