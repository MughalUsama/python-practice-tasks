import re
import sys


def validate_password(txt):
    _pattern = re.compile('(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,12}')
    for password in txt.split(","):
        if re.search(_pattern, password):
            print(password.strip())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        validate_password(sys.argv[1])
    else:
        text = 'ABd1234@1,a F1#,2w3E*,2We3345'
        validate_password(text)
