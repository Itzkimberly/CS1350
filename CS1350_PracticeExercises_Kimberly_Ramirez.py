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