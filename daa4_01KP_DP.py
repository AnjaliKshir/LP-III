# Function to solve 0-1 Knapsack problem
def knapsack_dp(weights, values, capacity):
    n = len(values)
    # Create a DP table with all values set to 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item or exclude it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value
    return dp[n][capacity]

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
    max_value = knapsack_dp(weights, values, capacity)
    print(f"Maximum value in knapsack = {max_value}")
