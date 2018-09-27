
class Node:
    '''
        Node Class
            get_value
            set_value
            set_next_node_value
    '''
    def __init__(self, value, next_node=None):
        '''
        Constructor class
        '''
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        '''
        return val of node
        '''
        return self.value
    
    def get_next_node(self):
        '''
        return val of next_node
        '''
        if self.next_node is not None:
            return self.next_node

        return None

    def set_next_node(self, next_node):
        self.next_node = next_node

my_node = Node(44)

# print(my_node.get_value())
# print(my_node.get_next_node())
# my_node.set_next_node(11)
# print(my_node.get_next_node())