import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_equal_01(self):
        print("HTMLNode 'Equals' Tests:")
        node1 = HTMLNode("href", "https://www.google.com", None, None)
        node2 = HTMLNode("href", "https://www.google.com")
        self.assertEqual(node1, node2)
        print("--Equals: Passed")
    def test_not_equals_01(self):
        print("HTMLNode 'Not Equals' Tests:")
        node1 = HTMLNode("href", "https://www.google.com")
        node2 = HTMLNode("href", "https://www.yahoo.com")
        self.assertNotEqual(node1, node2)
        print("--Not Equals: Passed")
    def test_props_to_html(self):
        print("HTMLNode: 'props_to_html'")
        test_node = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        processed_node = test_node.props_to_html()
        compare_node = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(compare_node, processed_node)
        print("-Props_to_HTML: Passed")

class TestLeafNode(unittest.TestCase):
    def test_equal_01(self):
        print("LeafNode 'Equals' Tests:")
        node1 = LeafNode("p", "This is a paragraph of text.").to_html()
        node2 = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node1, node2)
        print("--Equals 01: Passed")
        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        node4 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node3, node4)
        print("--Equals 02: Passed")

class TestParentNode(unittest.TestCase):
    def test_equal_01(self):
        print("ParentNode 'Equals' Tests:")
        node1 = ParentNode("p",[
            LeafNode("b","Bold text"),
            LeafNode(None,"Normal text"),
            LeafNode("i","italic text"),
            LeafNode(None,"Normal text"),]).to_html()
        node2 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node1, node2)
        print("--Equals 01: Passed")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        print("--Test with children: Passed")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")
        print("--Test with grandchildren: Passed")