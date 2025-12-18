stack = []     # empty stack

# Adding tasks (PUSH)
stack.append("Complete Python assignment")
stack.append("Clean the study table")
stack.append("Buy birthday gift")
stack.append("Prepare presentation for class")
stack.append("Reply to important email (URGENT)")

# Display all tasks (Top to Bottom)
print("\nAll Tasks (Top to Bottom):")
for task in reversed(stack):
    print("- ", task)

# Remove the most urgent task (POP)
print("\nMost urgent task completed:")
urgent_task = stack.pop()
print("✔", urgent_task)

# View the next top task (what to do next)
print("\nNext task to do:")
print("➡", stack[-1])

# Show updated task list
print("\nUpdated Task List (Top to Bottom):")
for task in reversed(stack):
    print("- ", task)
