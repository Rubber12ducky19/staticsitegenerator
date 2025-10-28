from textnode import TextNode, TextType

#print("Hello World")
def main(text, text_type, url):
    print(TextNode(text, text_type, url))

main("This is some anchor text",TextType.LINK, "https://www.boot.dev")
