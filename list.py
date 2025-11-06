# Example 1: Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

# Example 2: Even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", evens)

# Example 3: Convert list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)

# Example 4: Nested list comprehension - multiply elements of two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
product = [x*y for x in list1 for y in list2]
print("Products of elements:", product)

# Example 5: Filter words with length > 5
words = ["Python", "is", "awesome", "and", "fun"]
long_words = [word for word in words if len(word) > 5]
print("Words with length > 5:", long_words)
