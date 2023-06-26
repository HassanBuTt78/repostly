import re


def remove_non_bmp(text):
    return ''.join(c for c in text if ord(c) <= 0xFFFF)


def extract_tags_and_remove(string):
    tags = re.findall(r'#(\w+)', string)
    string_without_tags = re.sub(r'\s*#\w+\s*', ' ', string)
    return tags, string_without_tags.strip()
