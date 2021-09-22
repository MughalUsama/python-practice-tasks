import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Please enter comma separated numbers")
        else:
            arg_length = len(sys.argv[1])
            num_str = sys.argv[1]
            num_list = num_str.split(',')
            num_list = map(lambda x: int(x), num_list)
            new_list = [i ** 2 for i in num_list if i % 2 == 1]
            print(new_list)
    except ValueError:
        print("Please enter comma separated numbers only.")
