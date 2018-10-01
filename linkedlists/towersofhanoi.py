from stack import Stack

def optimalMoves(num_disks):
    # optimal moves for TOH
    return (2 ** num_disks) - 1

print("\nTowers of Hanoi\n")

# Create stacks
stacks = []
# for i in range(3):
#     stacks.append(Stack(str(i)))
stacks.append(Stack('Left'))
stacks.append(Stack('Center'))
stacks.append(Stack('Right'))



num_disks = int(input("\nHow many disks, guy?\n"))

while num_disks < 3:
    num_disks = int(input("\n How many disks, greater than 2"))

for i in range(num_disks, 0, -1): # step backwards by placing largest disks first on the left_stack
    stacks[0].push(i)


optimal_moves = optimalMoves(num_disks)
print("\nHey! TOH says for {} of disks the optimal amount of moves is {}".format(num_disks, optimal_moves))

# USER INPUT
def get_input():
    choices = {stack.get_name()[0]: stack for stack in stacks} # ['L', 'C', 'R']
    # import pdb; pdb.set_trace()
    # choices = [stack.get_name()[0] for stack in stacks] 
    while True: # infinite loop
        for stack in stacks:
            letter = stack.get_name()[0]
            name = stack.get_name()
            print('Enter {0} for {1}'.format(letter, stack.get_name()))
        user_input = input('Please enter a move')
        if user_input in choices:
            return choices[user_input]

num_user_moves = 0
right_stack = stacks[2]
def valid_move(from_stack, to_stack):
    pass

while right_stack.get_size() < num_disks:
    print("\n\n\n Current Stack \n\n\n")
    for stack in stacks:
        print(stack.print_items())
    
    while True:
        import pdb; pdb.set_trace()
        print("\n\nWhich stack would you like to move from?\n\n")
        from_stack = get_input()
        # import pdb; pdb.set_trace()
        print("\nWhich stack do you want to move to?")
        to_stack = get_input()
        print(type(from_stack))

        if from_stack.is_empty():
            print("\nInvalid move. Try again\n")
        elif to_stack.is_empty or from_stack.peek() < to_stack.peek():
            print('\n\nPrint. Hoorah\n\n')
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else: 
            print("\n\nCant move a larger disk onto a smaller disk. Invalid move. Try again\n\n")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, optimal_moves))


