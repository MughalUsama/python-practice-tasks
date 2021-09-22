import sys

# def capitalize_all_characters(a_string):
#   temp_str = ""
#    foreach(char in a_string):
#       temp_str = temp_str+char.upper()
#   return temp_str

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string.")
    else:
        print(sys.argv[1].upper())
