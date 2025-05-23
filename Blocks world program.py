def print_stacks(stacks):
    for i, stack in enumerate(stacks):
        print(f"Block(s) on stack: {stack}")
    print()

def move_block(stacks, from_stack, to_stack):
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)

# -----------------------------
# Initial state
initial_stacks = [[0], [1], [2]]
print("Initial state:")
print_stacks(initial_stacks)

# -----------------------------
# Define goal state
goal_stacks = [[0, 1], [2]]
print("Goal state set.")
print_stacks(goal_stacks)

# -----------------------------
# Perform moves to reach goal
print("Performing Moves:")

# Step 1: Move block 0 from stack 0 to stack 1
move_block(initial_stacks, 0, 1)
print_stacks(initial_stacks)

# Step 2: Move block 2 from stack 2 to stack 0
move_block(initial_stacks, 2, 0)
print_stacks(initial_stacks)

# Step 3: Move block 0 from stack 1 to stack 2
move_block(initial_stacks, 1, 2)
print_stacks(initial_stacks)

# Step 4: Move block 1 from stack 1 to stack 0
move_block(initial_stacks, 1, 0)
print_stacks(initial_stacks)

# Step 5: Move block 2 from stack 2 to stack 1
move_block(initial_stacks, 2, 1)
print_stacks(initial_stacks)
