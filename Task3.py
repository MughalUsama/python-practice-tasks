import sys


def create_dictionary(upper_limit):
    new_dict = dict()
    for i in range(1, upper_limit+1):
        new_dict[i] = i*i
    return new_dict


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Please enter Upper Limit")
        else:
            print(create_dictionary(int(sys.argv[1])))
    except ValueError:
        print("Please pass a number as upper bound.")
