import sys
print(sys.path.append('../'))


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
        item = NodeItem(value)
        item.set_next_node(self.top_item)
        self.top_item = item
    
    def peek(self):
        if not self.is_empty():
            return self.top_item
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
            return item_to_remove
        else: 
            print('Empty stack')
    
    def has_space(self):
        return self.size < self.limit
    
    def is_empty(self):
        return self.size == 0
    
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()