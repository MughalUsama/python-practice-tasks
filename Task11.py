import re
import sys


def remove_parentheses(txt):
    result = re.sub(r"\s*\((.*?)\)\s*|[\"\[\]]*", "", txt).split(",")
    # replaced either "(content)" or '"','[',']' with ""
    result = map(lambda s: s.strip(), result)
    print("\n".join(result))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        remove_parentheses(sys.argv[1])
    else:
        text = '["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]'
        remove_parentheses(text)
