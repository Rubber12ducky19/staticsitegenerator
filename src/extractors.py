import re

def extract_markdown_images(text):
    #takes raw markdown text and returns a list of tuples.
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    #matches should be a list of, (alt text, url)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    #matches should be a list of: (anchor text, url)
    return matches