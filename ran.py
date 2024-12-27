import random
n = 300
# Generate 300 unique random numbers from 1 to 1000
unique_numbers = random.sample(range(1, 10001), n)

# Print the result
print(unique_numbers)

for i in range(n-1):
    for j in range(n-1-i):
        if unique_numbers[j] > unique_numbers[j+1]:
            temp = unique_numbers[j+1]
            unique_numbers[j+1] = unique_numbers[j]
            unique_numbers[j] = temp
# print(unique_numbers)
for i in range(300):
    print(i, 'th: ',  unique_numbers[i])