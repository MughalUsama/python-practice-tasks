
if __name__ == "__main__":
    names_dict = dict()
    _file = open("names.txt")
    for line in _file:
        names_dict[line.strip()] = names_dict.get(line.strip(), 0) + 1

    for key, value in names_dict.items():
        print(key, value, sep=": ")
        