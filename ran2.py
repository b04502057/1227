import random

n = 30
# Generate 30 unique random numbers from 1 to 1000
unique_numbers = random.sample(range(1, 1001), n)

# Print the result
print("Original unique numbers:", unique_numbers)

# Bubble Sort
for i in range(n-1):
    for j in range(n-1-i):  # Adjusted loop range to ensure the last element is included
        if unique_numbers[j] > unique_numbers[j+1]:
            # Swap elements if they are in the wrong order
            unique_numbers[j], unique_numbers[j+1] = unique_numbers[j+1], unique_numbers[j]

# Print the sorted result
print("Sorted unique numbers:", unique_numbers)
