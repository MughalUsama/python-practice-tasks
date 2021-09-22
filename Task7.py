import re
import sys


def sort_words(txt):
    words_list = txt.split(",")
    words_list.sort()
    return ",".join(words_list)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sorted_words = sort_words(sys.argv[1])
        print(sorted_words)
    else:
        text = 'without,hello,bag,world'
        sorted_words = sort_words(text)
        print(sorted_words)
