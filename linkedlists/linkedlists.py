from node import Node as NodeClass

class LinkedList:
    def __init__(self, value=None):
        self.head_node = NodeClass(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        # import pdb; pdb.set_trace()
        new_node = NodeClass(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def traverse_list_and_output(self):
        node_list = []
        current_node = self.head_node
        while current_node:
            if current_node.value != None:
                node_list.append(str(current_node.value))
            current_node = current_node.get_next_node()
        return node_list
    
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node == self.head_node.get_next_node()
        else: 
            while current_node:
                # import pdb; pdb.set_trace()
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    break
                else: 
                    current_node = next_node


linnk = LinkedList(5)
linnk.insert_beginning(44)
linnk.insert_beginning(300)
linnk.insert_beginning(400)
linnk.insert_beginning(500)

linnk.remove_node(44)
print(linnk.traverse_list_and_output())