class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight 

# Function to calculate the maximum value that can be carried
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)
    
    total_value = 0.0  # To store the total value
    
    for item in items:
        if capacity >= item.weight:
            # If the item can fit in the remaining capacity, take it all
            capacity -= item.weight
            total_value += item.value
        else:
            # Otherwise, take the fraction of the item that fits
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break  # The knapsack is full
    
    return total_value

# Driver code to take input from the user
if __name__ == "__main__":
    # Taking input for the number of items
    num_items = int(input("Enter the number of items: "))
    
    items = []
    
    # Taking input for the value and weight of each item
    for i in range(num_items):
        value = float(input(f"Enter value for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(value, weight))
    
    # Taking input for the capacity of the knapsack
    capacity = float(input("Enter the capacity of the knapsack: "))
    
    # Calculate and print the maximum value
    max_value = fractional_knapsack(items, capacity)
    print(f"\nMaximum value we can obtain = {max_value:.2f}")
