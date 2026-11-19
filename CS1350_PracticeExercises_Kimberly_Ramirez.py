# ==========================================
# Exercise 2.3: Filter and Sort
# ==========================================
words = ["kiwi", "fig", "banana", "plum", "apple"]

# TODO 1: Use filter and a lambda to keep words with more than 4 letters
long_words = list(filter(lambda w: len(w) > 4, words))
print("Long words:", long_words)  # ['banana', 'apple']

# TODO 2: Use sorted() with key=lambda to order words by length
by_length = sorted(words, key=lambda w: len(w))
print("Sorted by length:", by_length)   # ['fig', 'kiwi', 'plum', 'apple', 'banana']


# ==========================================
# Exercise 2.4: Make an Object Callable
# ==========================================
class Adder:
    def __init__(self, amount):
        self.amount = amount

    def __call__(self, value):
        """Make instance callable like a function"""
        return value + self.amount

add_ten = Adder(10)
print("Result of add_ten(5):", add_ten(5))        # 15
print("Is add_ten callable?:", callable(add_ten)) # True


# ==========================================
# Exercise 3.1: Add the Missing Line
# ==========================================
def count_up_to(n):
    """Yield 1, 2, 3, ..., up to n."""
    i = 1
    while i <= n:
        yield i  # Hand back i with yield
        i += 1

print("Count up to 3:", list(count_up_to(3)))  # [1, 2, 3]
gen = count_up_to(2)
print("Next from gen:", next(gen))             # 1
print("Next from gen:", next(gen))             # 2


# ==========================================
# Exercise 3.2: From List to Generator
# ==========================================
# Changed list comprehension brackets [] into generator expression parentheses ()
squares = (x * x for x in range(5))

print("Squares next(0):", next(squares))         # 0
print("Squares next(1):", next(squares))         # 1
print("Squares remaining list:", list(squares))  # [4, 9, 16]