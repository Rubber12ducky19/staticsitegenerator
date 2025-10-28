class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag # A string representing the HTML tag name
        self.value = value # A string representing the value of the HTML tag
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag.

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return "" #If there are no props, return a blank string
        #Retuns a string that represents the HTML attributes of the node.
        if isinstance(self.props, dict):
            #if self.props is a dictionary
            parts = [f'{key}="{value}"' for key, value in self.props.items()]
            #for each key-value pair in self.props, make a list called parts
            return "" + " ".join(parts) # Joins the parts list into a string with spacing.
        raise Exception("self.props is not a dictionary")
    
    def __repr__(self):
        print(f"HTMLNode(tag= {self.tag}, value= {self.value}, children= {self.children}, props= {self.props}")
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag is None:
            return self.value
        elif self.props_to_html() == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All Parent Nodes must have a tag")
        elif self.children is None:
            raise ValueError("All Parent Nodes must have a child")
        elif len(self.children) == 0:
            raise ValueError("All Parent Nodes must have a child, Children list is empty")
        children_list = []
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise Exception("Child in list is not a HTMLNode")
            else:
                children_list.append(child.to_html())
        children_result = "".join(children_list)
        if self.props_to_html() == "":
            return f"<{self.tag}>{children_result}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{children_result}</{self.tag}>"
        