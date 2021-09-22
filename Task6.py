import sys


def calculate_digits_and_letters(sentence):
    digits_count = 0
    letters_count = 0
    for character in sentence:
        if str.isdigit(character):
            digits_count += 1
        elif str.isalpha(character):
            letters_count += 1
    return digits_count, letters_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string.")
    else:
        digit_count, letter_count = calculate_digits_and_letters(sys.argv[1])
        print("LETTERS", letter_count)
        print("DIGITS", digit_count)
