from queue import PriorityQueue

# Node structure for Branch and Bound
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    # For priority queue (max heap) comparison
    def __lt__(self, other):
        return self.bound > other.bound

# Function to calculate upper bound on maximum profit in subtree rooted with 'node'
def calculate_bound(node, n, capacity, values, weights):
    if node.weight >= capacity:
        return 0  # No bound if weight exceeds capacity

    # Initial profit bound is the current profit
    profit_bound = node.profit
    total_weight = node.weight
    j = node.level + 1

    # Add items to the knapsack while there's capacity
    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1

    # Add fractional part of the next item (if any)
    if j < n:
        profit_bound += (capacity - total_weight) * (values[j] / weights[j])

    return profit_bound

# Function to solve 0-1 Knapsack problem using Branch and Bound
def knapsack_bb(values, weights, capacity):
    n = len(values)
    q = PriorityQueue()

    # Sort items by value-to-weight ratio
    items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    sorted_weights = [weights[i] for i in items]
    sorted_values = [values[i] for i in items]

    # Create a dummy node at the root and calculate its bound
    u = Node(-1, 0, 0, 0)
    u.bound = calculate_bound(u, n, capacity, sorted_values, sorted_weights)
    q.put(u)
    
    max_profit = 0

    # Priority queue processing
    while not q.empty():
        u = q.get()

        # Only proceed if the node's bound is better than the current max profit
        if u.bound > max_profit and u.level < n - 1:
            # Branch to include the next item
            v = Node(u.level + 1, 0, 0, 0)

            # Case 1: Include the next item
            v.weight = u.weight + sorted_weights[v.level]
            v.profit = u.profit + sorted_values[v.level]

            if v.weight <= capacity and v.profit > max_profit:
                max_profit = v.profit

            v.bound = calculate_bound(v, n, capacity, sorted_values, sorted_weights)
            if v.bound > max_profit:
                q.put(v)

            # Case 2: Exclude the next item
            v.weight = u.weight  # No change in weight
            v.profit = u.profit  # No change in profit
            v.bound = calculate_bound(v, n, capacity, sorted_values, sorted_weights)
            if v.bound > max_profit:
                q.put(v)

    return max_profit

# Main function to get input and solve the problem
if __name__ == "__main__":
    # Get the number of items
    n = int(input("Enter number of items: "))

    # Get the weights and values of the items
    weights = list(map(int, input("Enter weights separated by space: ").split()))
    values = list(map(int, input("Enter values separated by space: ").split()))

    # Get the knapsack capacity
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Solve and print the maximum value
    max_value = knapsack_bb(values, weights, capacity)
    print(f"Maximum value in knapsack = {max_value}")
