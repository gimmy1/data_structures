from node import Node as NodeItem

class Stack:
    '''
    FILO
    push()
    pop()
    peek()

    # helper methods - is_empty, has_space
    '''
    def __init__(self, top_item, limit=100, size=0):
        self.top_item = top_item
        self.limit = limit
        self.size = size

    def push(self, value):
        '''
        turn value into Node
        set node.next to top_item
        top_item = item
        '''
        if self.has_space():
            item = NodeItem(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))
    
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print('Empty stack')

    def pop(self):
        '''
        return top_item
        turn top_item into the next_node of top item
        if self.size > 0
        '''
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else: 
            print('Empty stack')
    
    def has_space(self):
        return self.size < self.limit
    
    def is_empty(self):
        return self.size == 0
    
# Defining an empty stack
stack = Stack(6)
print(stack)
# Adding as they are ready until we have 
# stack.push("#1")
# stack.push("#2")
# stack.push("#3")
# stack.push("#4")
# stack.push("#5")
# stack.push("#6")

# Uncomment the push() statement below:
# stack.push("#7")

# Delivering from the top of the stack down
# print("The first to deliver is " + stack.peek())
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

stack.pop()