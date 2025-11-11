from textnode import TextNode, TextType
from extractors import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #Takes a list of "old nodes", a delimiter, and a text type.  Should return a new list of nodes,
    #where any "text" type nodes in the input are (potentially) split into multiple nodes based on 
    #the syntax.

    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            node_list = node.text.split(delimiter) #For each node in "old nodes", if it matches the text type,
            # split the node into a new list, seperated by the "delimiter"
            if len(node_list) %2 == 0: #Checks if the "node list" has a opening, middle, and close. (Odd number length)
                raise Exception("Delimiter not closing")
            for index in range(len(node_list)):
                if node_list[index] != "": #Checks if it isn't empty:
                    if index %2 == 0:
                        new_nodes.append(TextNode(node_list[index], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(node_list[index], text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue
        for alt, url in images:
            before, sep, after = text.partition(f"![{alt}]({url})")
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = after
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue
        for anchor, url in links:
            before, sep, after = text.partition(f"[{anchor}]({url})")
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            text = after
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes