import statistics # Optional: python has a cheat code for mode!

# 1. Get Input
text = input("Enter numbers separated by space: ")
words = text.split()

# 2. Convert to Integers
numbers = []
for word in words:
    numbers.append(int(word))

# 3. Mean
mean = sum(numbers) / len(numbers)

# 4. Median
numbers.sort()
index = len(numbers) // 2 # Use // for integer
median = numbers[index]

# 5. Mode
mode = max(numbers, key=numbers.count)

# 6. Print
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)