def backward_chaining(rules, facts, goal, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for rule in rules:
        head = rule[0]
        body = rule[1:]

        if head == goal:
            if all(backward_chaining(rules, facts, subgoal, visited) for subgoal in body):
                facts.add(goal)
                return True
    return False

# -----------------------------------
# Define the knowledge base (rules)
# Format: [conclusion, premise1, premise2, ...]
rules = [
    ['a'],
    ['b'],
    ['c', 'a', 'b'],   # c ← a ∧ b
    ['d', 'b'],        # d ← b
]

# Initial facts (atomic facts without rules)
facts = set(['a', 'b'])

# -----------------------------------
# Test goals with expected outputs
# -----------------------------------
goals = ['f', 'd']

for goal in goals:
    result = backward_chaining(rules, facts.copy(), goal)
    if result:
        print(f"The goal '{goal}' can be achieved.")
    else:
        print(f"The goal '{goal}' cannot be achieved.")
