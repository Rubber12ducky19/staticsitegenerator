import unittest
from textnode import TextNode,TextType
from delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

class Test_Split_Nodes_Delimiter(unittest.TestCase):
    def test_01(self):
        print("Split Nodes:\n-Test One:")
        test_node = [TextNode("This is a text node with a 'code block' in it.", TextType.TEXT)]
        node = split_nodes_delimiter(test_node,"'", TextType.CODE)
        compare_results = [TextNode("This is a text node with a ", TextType.TEXT),
                           TextNode("code block", TextType.CODE),
                           TextNode(" in it.", TextType.TEXT)]
        self.assertEqual(node, compare_results)
        
    def test_02(self):
        print("Split Nodes:\n-Test Two:")
        test_node = [TextNode("This is a text node with 'two' types of 'code blocks' in it.", TextType.TEXT)]
        node =  split_nodes_delimiter(test_node, "'", TextType.CODE)
        compare_results = [TextNode("This is a text node with ", TextType.TEXT),
                           TextNode("two", TextType.CODE),
                           TextNode(" types of ", TextType.TEXT),
                           TextNode("code blocks", TextType.CODE),
                           TextNode(" in it.", TextType.TEXT)]
        self.assertEqual(node, compare_results)

    def test_03(self):
        print("Split Nodes:\n-Test Three: Multi-Split")
        test_node = [TextNode("This is a **large** text node _with multiple_ types of splits `going on` in it.", TextType.TEXT)]
        node_bold = split_nodes_delimiter(test_node, "**", TextType.BOLD)
        node_italic = split_nodes_delimiter(node_bold, "_", TextType.ITALIC)
        node_code = split_nodes_delimiter(node_italic, "`", TextType.CODE)
        compare_results = [TextNode("This is a ",TextType.TEXT),
                           TextNode("large", TextType.BOLD),
                           TextNode(" text node ", TextType.TEXT),
                           TextNode("with multiple", TextType.ITALIC),
                           TextNode(" types of splits ", TextType.TEXT),
                           TextNode("going on", TextType.CODE),
                           TextNode(" in it.", TextType.TEXT)]
        self.assertEqual(node_code, compare_results)
    
    def test_04(self):
        print("Split Nodes:\n-Test Four: Multi-Split(Unordered)")
        test_node = [TextNode("This is a **large** text node _with multiple_ types of splits `going on` in it.", TextType.TEXT)]
        node_code = split_nodes_delimiter(test_node, "`", TextType.CODE)
        node_bold = split_nodes_delimiter(node_code, "**", TextType.BOLD)
        node_italic = split_nodes_delimiter(node_bold, "_", TextType.ITALIC)
        compare_results = [TextNode("This is a ",TextType.TEXT),
                           TextNode("large", TextType.BOLD),
                           TextNode(" text node ", TextType.TEXT),
                           TextNode("with multiple", TextType.ITALIC),
                           TextNode(" types of splits ", TextType.TEXT),
                           TextNode("going on", TextType.CODE),
                           TextNode(" in it.", TextType.TEXT)]
        self.assertEqual(node_italic, compare_results)
    
    def test_05(self):
        print("Split Nodes:\n-Test Five: Empty Node")
        test_node = [TextNode("This is a text node __ with bad formating `` and should only be text nodes ****", TextType.TEXT)]
        node_italic = split_nodes_delimiter(test_node, "_", TextType.ITALIC)
        node_bold = split_nodes_delimiter(node_italic, "**", TextType.BOLD)
        node_code = split_nodes_delimiter(node_bold, "`", TextType.CODE)
        compare_results = [TextNode("This is a text node ", TextType.TEXT),
                           TextNode(" with bad formating ", TextType.TEXT),
                           TextNode(" and should only be text nodes ", TextType.TEXT)]
        self.assertEqual(node_code, compare_results)

class Test_Split_Nodes_ImgAndLink(unittest.TestCase):
    def test_01(self):
        print("Split Nodes:\n-Images Test 01")
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes,)
        
    def test_02(self):
        print("Split Nodes:\n-Images Test 02(No Image)")
        node = TextNode("This is a text with no images",TextType.TEXT)  
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is a text with no images",TextType.TEXT)], new_nodes)

    def test_03(self):
        print("Split Nodes:\n-Images & Link Test 01")
        node = TextNode("This is a text node with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](www.google.com)", TextType.TEXT)
        image_nodes = split_nodes_image([node])
        link_nodes = split_nodes_link(image_nodes)
        self.assertListEqual([
            TextNode("This is a text node with an ", TextType.TEXT),
            TextNode("image",TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "www.google.com")
        ], link_nodes)

    def test_04(self):
        print("Split Nodes:\n-Images, Links, and skipped nodes")
        node = TextNode("This is a **Text** node with a ![image](https://i.imgur.com/zjjcJKZ.png), some _italic text_, and a [link](www.google.com)", TextType.TEXT)
        imaged_nodes = split_nodes_image([node])
        linked_nodes = split_nodes_link(imaged_nodes)
        self.assertListEqual([
            TextNode("This is a **Text** node with a ", TextType.TEXT),
            TextNode("image",TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(", some _italic text_, and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "www.google.com")
        ], linked_nodes)
        print("-With Nodes")
        bolded_nodes = split_nodes_delimiter(linked_nodes,"**", TextType.BOLD)
        italiced_nodes = split_nodes_delimiter(bolded_nodes, "_", TextType.ITALIC)
        self.assertListEqual([
            TextNode("This is a ", TextType.TEXT),
            TextNode("Text", TextType.BOLD),
            TextNode(" node with a ", TextType.TEXT),
            TextNode("image",TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(", some ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(", and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "www.google.com")], italiced_nodes)