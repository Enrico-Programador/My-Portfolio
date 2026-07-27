import re


def convert_exception(file_data):
    pattern = r":::hero(.*?):::"
    match = re.search(pattern, file_data, re.DOTALL)
    if match == None:
        return match

    print(match.group(0))