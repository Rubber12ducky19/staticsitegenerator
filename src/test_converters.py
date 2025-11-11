import unittest
from textnode import TextNode,TextType
from converters import text_node_to_html_node, text_to_textnodes

class Test_TextNode_to_HTMLNode(unittest.TestCase):
    def test_text(self):
        print("TextNode to HTMLNode Tests:\n-Text:")
        node = text_node_to_html_node(TextNode("This is a text node", TextType.TEXT))
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "This is a text node")
    
    def test_bold(self):
        print("TextNode to HTMLNode Tests:\n-Bold:")
        node = text_node_to_html_node(TextNode("This is a bold node", TextType.BOLD))
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "This is a bold node")
    
    def test_italic(self):
        print("TextNode to HTMLNode Tests:\n-Italic:")
        node = text_node_to_html_node(TextNode("This is a italic node", TextType.ITALIC))
        self.assertEqual(node.tag, "i")
        self.assertEqual(node.value, "This is a italic node")
    
    def test_node(self):
        print("TextNode to HTMLNode Tests:\n-Code:")
        node = text_node_to_html_node(TextNode("This is a code node", TextType.CODE))
        self.assertEqual(node.tag, "code")
        self.assertEqual(node.value, "This is a code node")
    
    def test_link(self):
        print("TextNode to HTMLNode Tests:\n-Link:")
        node = text_node_to_html_node(TextNode("This is a link node", TextType.LINK, "https://www.yahoo.com"))
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "This is a link node")
        self.assertEqual(node.props, {"href": "https://www.yahoo.com"})

    def test_link_fail(self):
        print("TextNode to HTMLNode Tests:\n-Link(Failure):")
        node = TextNode("This is a link node that should fail", TextType.LINK)
        self.assertRaises(Exception, text_node_to_html_node, node)
    
    def test_image(self):
        print("TextNode to HTMLNode Tests:\n-Image:")
        node = text_node_to_html_node(TextNode("This is a image node", TextType.IMAGE, "https://www.google.com"))
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src":"https://www.google.com","alt":"This is a image node"})

    def test_image_fail(self):
        print("TextNode to HTMLNode Tests:\n-Image(Failure):")
        node = TextNode("This is a image node that should fail", TextType.IMAGE)
        self.assertRaises(Exception, text_node_to_html_node, node)

class Test_Text_to_TextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        print("Text to TextNode:\n-Test One")
        node = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),], node)
