import re

from markdown_to_html import markdown_to_html_node
from splitnode import text_to_textnodes


def convert_exception(file_data):
    match = re.search(r":::hero(.*?):::", file_data, re.DOTALL)
    if match == None:
        return file_data
    hero = match.group(1)
    lines = hero.splitlines()
    formatted = '<section class="hero">'
    lines.append('</div></section>')
    for line in lines:
        if line.startswith(("![")):
            formatted = formatted + line + '<div class="hero-content">'
            continue
        formatted = formatted + line
    print(file_data.replace(match.group(0), formatted))
    return file_data.replace(match.group(0), formatted)
    