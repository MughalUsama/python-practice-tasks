
def divisible_by_7_not_by_5(low_limit, upper_limit):
    temp_list = list()
    for i in range(low_limit, upper_limit+1):
        if i % 7 == 0 and i % 5 != 0:
            temp_list.append(i)
    return temp_list


if __name__ == "__main__":
    lst = divisible_by_7_not_by_5(1000, 2000)
    print(*lst, sep=", ")

# can be done by printing each value in loop but used list to automatically unpack values and separate by "," without
# adding comma at the end.
