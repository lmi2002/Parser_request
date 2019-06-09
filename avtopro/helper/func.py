import re


def delete_sym(s):
    return re.sub(r'\W+', "", s)