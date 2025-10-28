from textnode import TextNode, TextType
from htmlnode import LeafNode

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