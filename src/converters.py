from textnode import TextNode, TextType
from htmlnode import LeafNode
from delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_node_to_html_node(text_node):
    #Should handle each type of TextType enum.  If gets a TextNode, that is none of those types, it should raise an Exception.
    #Otherwise, it should return a new LeafNode object.
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            if text_node.url:
                return LeafNode("a", text_node.text, {"href":text_node.url})
            else: raise Exception("TextNode Link has no url")
        case TextType.IMAGE:
            if text_node.url:
                return LeafNode("img","",{"src":text_node.url, "alt":text_node.text})
            else: raise Exception("TextNode Image has no url")
        case _:
            raise Exception("TextNode has no supported TextType enum")

def text_to_textnodes(text):
    #Should take a string of Markdown text and return a list of TextNodes objects.
    first_node = [TextNode(text, TextType.TEXT),]
    imaged_node = split_nodes_image(first_node)
    linked_node = split_nodes_link(imaged_node)
    bolded_node = split_nodes_delimiter(linked_node, "**", TextType.BOLD)
    italiced_node = split_nodes_delimiter(bolded_node, "_", TextType.ITALIC)
    coded_node = split_nodes_delimiter(italiced_node, "`", TextType.CODE)
    return coded_node
