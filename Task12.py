import re
import sys


def find_urls(txt):
    result = re.findall(r"https?://\S+", txt)
    return result



if __name__ == "__main__":
    if len(sys.argv) > 1:
        urls_list = find_urls(sys.argv[1])
        print(urls_list)
    else:
        text = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of ' \
               'http://www.geeksforgeeks.org'
        urls_list = find_urls(text)
        print(urls_list)
