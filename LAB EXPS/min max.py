import math

# Min-Max Function
def minimax(depth, nodeIndex, isMax, values, height):

    # Base condition
    if depth == height:
        return values[nodeIndex]

    # MAX Player
    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )

    # MIN Player
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )


# User Input
n = int(input("Enter the number of leaf nodes (must be a power of 2): "))

values = []

print("Enter the leaf node values:")

for i in range(n):
    value = int(input(f"Value {i + 1}: "))
    values.append(value)

# Calculate tree height
height = int(math.log2(n))

# Find optimal value
result = minimax(0, 0, True, values, height)

# Display Output
print("\nLeaf Node Values:", values)
print("Optimal Value:", result)
