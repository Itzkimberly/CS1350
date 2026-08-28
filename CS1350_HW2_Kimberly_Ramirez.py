"""
CS1350_HW2_FirstName_LastName.py
Homework 2: Dictionaries Basics
Due: Mon Aug 31, 2026 8:00am
CS1350 - Computer Science II
"""

# ============================================================
# UNIT 1.1: What Are Dictionaries?
# ============================================================

# ----- Beginner (5 pts) -----
# Create a dictionary called my_info with:
#   - Your first name as key "name"
#   - Your age as key "age"
#   - Your major as key "major"
def exercise_1_1_beginner():
    print("=" * 50)
    print("Unit 1.1 - Beginner: Creating a Personal Info Dictionary")
    print("=" * 50)

    my_info = {
        "name": "Kim",
        "age": 20,
        "major": "Cybersecurity"
    }

    print("my_info =", my_info)
    print("Name:", my_info["name"])
    print("Age:", my_info["age"])
    print("Major:", my_info["major"])
    print()
    return my_info


# ----- Intermediate (10 pts) -----
# 1. Create a dictionary 'menu' with at least 4 food items and their prices.
# 2. Create a dictionary 'course_credits' mapping course names to credit hours.
def exercise_1_1_intermediate():
    print("=" * 50)
    print("Unit 1.1 - Intermediate: Menu and Course Credits Dictionaries")
    print("=" * 50)

    # Task 1: Menu dictionary
    menu = {
        "burger": 8.99,
        "fries": 3.49,
        "soda": 1.99,
        "salad": 6.49
    }
    print("Menu:")
    for item, price in menu.items():
        print("  {}: ${:.2f}".format(item, price))

    # Task 2: Course credits dictionary
    course_credits = {
        "CS1350": 3,
        "MATH201": 4,
        "ENG101": 3,
        "PHYS150": 4
    }
    print("\nCourse Credits:")
    for course, credits in course_credits.items():
        print("  {}: {} credits".format(course, credits))
    print()
    return menu, course_credits


# ----- Advanced (15 pts) -----
# Create a dictionary 'weekly_temps' that maps each day of the week 
# to a temperature. Use the dict() function instead of curly braces.
def exercise_1_1_advanced():
    print("=" * 50)
    print("Unit 1.1 - Advanced: Weekly Temperatures using dict()")
    print("=" * 50)

    weekly_temps = dict(
        Monday=72,
        Tuesday=75,
        Wednesday=68,
        Thursday=80,
        Friday=77,
        Saturday=82,
        Sunday=70
    )

    print("Weekly Temperatures (created with dict()):")
    for day, temp in weekly_temps.items():
        print("  {}: {} F".format(day, temp))
    print()
    return weekly_temps


# ============================================================
# UNIT 1.2: Accessing Dictionary Elements
# ============================================================

# ----- Beginner (5 pts) -----
# Given: pet = {"name": "Buddy", "type": "dog", "age": 3}
# Write code to print the pet's name and type.
def exercise_1_2_beginner():
    print("=" * 50)
    print("Unit 1.2 - Beginner: Accessing Dictionary Elements")
    print("=" * 50)

    pet = {"name": "Buddy", "type": "dog", "age": 3}

    print("Pet Name:", pet["name"])
    print("Pet Type:", pet["type"])
    print()
    return pet


# ----- Intermediate (10 pts) -----
# 1. Given the pet dictionary above, use get() to safely access the "color" 
#    key (which doesn't exist). Print a default of "unknown".
# 2. Create code that checks if a student passed a course. Use get() with 
#    a grades dictionary.
def exercise_1_2_intermediate():
    print("=" * 50)
    print("Unit 1.2 - Intermediate: Safe Dictionary Access with get()")
    print("=" * 50)

    # Task 1: Safe access with default
    pet = {"name": "Buddy", "type": "dog", "age": 3}
    color = pet.get("color", "unknown")
    print("Pet color:", color)

    # Task 2: Check if student passed using get()
    grades = {"CS1350": 85, "MATH201": 72, "ENG101": 68}
    course = "CS1350"
    grade = grades.get(course, None)

    if grade is None:
        print("Student is not enrolled in", course)
    elif grade >= 70:
        print("Student PASSED {} with grade {}".format(course, grade))
    else:
        print("Student FAILED {} with grade {}".format(course, grade))

    # Test with a course not in the dictionary
    missing_course = "PHYS150"
    missing_grade = grades.get(missing_course, None)
    if missing_grade is None:
        print("Student is not enrolled in", missing_course)
    print()
    return grades


# ----- Advanced (15 pts) -----
# Write code that takes a products dictionary and a product name.
# Print the price if found, or "Product not available" if not found.
# Test with both existing and non-existing products.
def exercise_1_2_advanced():
    print("=" * 50)
    print("Unit 1.2 - Advanced: Product Price Lookup with get()")
    print("=" * 50)

    products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

    def lookup_price(product_dict, product_name):
        price = product_dict.get(product_name)
        if price is not None:
            print("{}: ${:.2f}".format(product_name, price))
        else:
            print("{}: Product not available".format(product_name))

    # Test with existing product
    lookup_price(products, "laptop")
    lookup_price(products, "mouse")

    # Test with non-existing product
    lookup_price(products, "monitor")
    lookup_price(products, "headphones")
    print()
    return products


# ============================================================
# UNIT 1.3: Modifying Dictionaries
# ============================================================

# ----- Beginner (5 pts) -----
# Start with an empty dictionary called inventory = {}.
# Add three items with their quantities (e.g., "apples": 5).
def exercise_1_3_beginner():
    print("=" * 50)
    print("Unit 1.3 - Beginner: Adding Items to an Empty Dictionary")
    print("=" * 50)

    inventory = {}
    inventory["apples"] = 50
    inventory["bananas"] = 30
    inventory["oranges"] = 25

    print("Inventory after adding items:")
    for item, qty in inventory.items():
        print("  {}: {}".format(item, qty))
    print()
    return inventory


# ----- Intermediate (10 pts) -----
# Given: scores = {"Team A": 45, "Team B": 38}
# 1. Update Team B's score to 52 and add "Team C" with 41 points.
# 2. Remove "Team A" using pop() and print what score they had.
def exercise_1_3_intermediate():
    print("=" * 50)
    print("Unit 1.3 - Intermediate: Updating and Removing Dictionary Entries")
    print("=" * 50)

    scores = {"Team A": 45, "Team B": 38}
    print("Original scores:", scores)

    # Task 1: Update Team B and add Team C
    scores["Team B"] = 52
    scores["Team C"] = 41
    print("After updates:", scores)

    # Task 2: Remove Team A using pop()
    removed_score = scores.pop("Team A")
    print("Team A was removed. Their score was:", removed_score)
    print("Final scores:", scores)
    print()
    return scores


# ----- Advanced (15 pts) -----
# Create a simple shopping cart system:
# 1. Start with an empty cart dictionary
# 2. Add 3 items with prices
# 3. Update the price of one item
# 4. Remove one item and print what was removed
# 5. Print the final cart
# Bonus: Calculate and print the total price of remaining items.
def exercise_1_3_advanced():
    print("=" * 50)
    print("Unit 1.3 - Advanced: Shopping Cart System")
    print("=" * 50)

    # Step 1: Start with empty cart
    cart = {}

    # Step 2: Add 3 items with prices
    cart["milk"] = 3.49
    cart["bread"] = 2.99
    cart["eggs"] = 4.29
    print("Cart after adding items:", cart)

    # Step 3: Update the price of one item
    cart["milk"] = 3.99
    print("After updating milk price:", cart)

    # Step 4: Remove one item and print what was removed
    removed = cart.pop("bread")
    print("Removed bread (price was ${:.2f})".format(removed))

    # Step 5: Print the final cart
    print("Final cart:", cart)

    # Bonus: Calculate total price of remaining items
    total = sum(cart.values())
    print("Total price of remaining items: ${:.2f}".format(total))
    print()
    return cart


# ============================================================
# UNIT 2.1: How Dictionaries Work
# ============================================================

# ----- Beginner (5 pts) -----
# Which of these are valid dictionary keys? Write "valid" or "invalid" 
# and explain why:
# a) "student_name"  b) [1, 2, 3]  c) 100  d) ("x", "y")  e) {"a": 1}  f) frozenset({1, 2})
def exercise_2_1_beginner():
    print("=" * 50)
    print("Unit 2.1 - Beginner: Valid vs Invalid Dictionary Keys")
    print("=" * 50)

    key_analysis = [
        ('"student_name"', "VALID", "Strings are immutable and hashable."),
        ("[1, 2, 3]", "INVALID", "Lists are mutable (can be changed after creation), so they cannot be hashed."),
        ("100", "VALID", "Integers are immutable and hashable."),
        ('("x", "y")', "VALID", "Tuples are immutable and hashable (as long as their contents are hashable)."),
        ('{"a": 1}', "INVALID", "Dictionaries are mutable, so they cannot be hashed."),
        ("frozenset({1, 2})", "VALID", "Frozensets are immutable versions of sets and are hashable."),
    ]

    for key, status, reason in key_analysis:
        print("  {:25} -> {:8} ({})".format(key, status, reason))
    print()


# ----- Intermediate (10 pts) -----
# 1. This code has an error. Find and fix it:
#    locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}
# 2. What will this print? Predict the output, then verify:
#    data = {"a": 1, "b": 2, "a": 3, "b": 4}
#    print(data)
#    print(len(data))
# 3. Investigate: What is the hash value of your name? What about the number 100?
def exercise_2_1_intermediate():
    print("=" * 50)
    print("Unit 2.1 - Intermediate: Fixing Errors and Investigating Hashing")
    print("=" * 50)

    # Task 1: Fix the error - lists cannot be keys, but tuples can!
    print("Task 1: Fixed locations dictionary")
    locations = {
        (40.7, -74.0): "New York",
        (34.0, -118.2): "Los Angeles"
    }
    print("  locations =", locations)
    print("  New York coordinates:", locations[(40.7, -74.0)])

    # Task 2: Predict and verify duplicate keys behavior
    print("\nTask 2: Duplicate keys behavior")
    print("  Prediction: data will have 2 items (last values win silently)")
    data = {"a": 1, "b": 2, "a": 3, "b": 4}
    print("  data =", data)
    print("  len(data) =", len(data))
    print("  Explanation: When duplicate keys exist, the last assignment wins.")

    # Task 3: Hash values investigation
    print("\nTask 3: Hash values")
    name = "Alex"
    print("  hash('{}') = {}".format(name, hash(name)))
    print("  hash(100) =", hash(100))
    print("  Note: hash values may vary between Python sessions.")
    print()


# ----- Advanced (15 pts) -----
# 1. Create a dictionary that tracks game high scores using tuples as keys 
#    where each tuple contains (player_name, game_name), and values are the scores.
#    Add at least 3 entries and retrieve one.
# 2. Write code that compares the time to check if an element exists in a list 
#    vs a dictionary with 100,000 elements. Print which is faster and by how much.
def exercise_2_1_advanced():
    print("=" * 50)
    print("Unit 2.1 - Advanced: Tuple Keys and Performance Comparison")
    print("=" * 50)

    import time

    # Task 1: High scores with tuple keys
    print("Task 1: Game High Scores with Tuple Keys")
    high_scores = {
        ("Alice", "Tetris"): 15000,
        ("Bob", "Pac-Man"): 25000,
        ("Carol", "Space Invaders"): 18000,
        ("Alice", "Pac-Man"): 22000
    }

    print("  High Scores:")
    for (player, game), score in high_scores.items():
        print("    {} in {}: {}".format(player, game, score))

    # Retrieve one specific score
    lookup = ("Bob", "Pac-Man")
    print("\n  Retrieving {}: {}".format(lookup, high_scores[lookup]))

    # Task 2: Performance comparison
    print("\nTask 2: List vs Dictionary Lookup Performance (100,000 elements)")

    n = 100000
    big_list = list(range(n))
    big_dict = {i: i for i in range(n)}
    target = 99999

    # List lookup
    start = time.time()
    result = target in big_list
    list_time = time.time() - start

    # Dictionary lookup
    start = time.time()
    result = target in big_dict
    dict_time = time.time() - start

    print("  List search time:       {:.8f} seconds".format(list_time))
    print("  Dictionary search time: {:.8f} seconds".format(dict_time))

    if dict_time > 0:
        speedup = list_time / dict_time
        print("  Dictionary is ~{:.0f}x faster than list!".format(speedup))
    else:
        print("  Dictionary is significantly faster (dict time too small to measure precisely)")
    print()


# ============================================================
# UNIT 2.2: The keys() and values() Methods
# ============================================================

# ----- Beginner (5 pts) -----
# Given: temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
# Write code to:
# 1. Print all the day names using keys()
# 2. Print all the temperatures using values()
# 3. Print how many days are in the dictionary
def exercise_2_2_beginner():
    print("=" * 50)
    print("Unit 2.2 - Beginner: Using keys() and values() Methods")
    print("=" * 50)

    temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

    # Task 1: Print all day names using keys()
    print("Day names (keys()):")
    for day in temps.keys():
        print("  ", day)

    # Task 2: Print all temperatures using values()
    print("\nTemperatures (values()):")
    for temp in temps.values():
        print("  ", temp, "F")

    # Task 3: Print how many days
    print("\nNumber of days:", len(temps))
    print()
    return temps


# ----- Intermediate (10 pts) -----
# 1. Find and print the highest and lowest temperatures from temps.
# 2. Check if "Friday" is in the dictionary using the in operator. Print an appropriate message.
# 3. Use setdefault() to add "Thursday" with a value of 70, but only if it doesn't exist.
# 4. Demonstrate that views are dynamic: create a keys view, add a new day, show the view updated.
def exercise_2_2_intermediate():
    print("=" * 50)
    print("Unit 2.2 - Intermediate: Dictionary Methods and Dynamic Views")
    print("=" * 50)

    temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

    # Task 1: Highest and lowest temperatures
    print("Highest temperature:", max(temps.values()), "F")
    print("Lowest temperature:", min(temps.values()), "F")

    # Task 2: Check if "Friday" is in the dictionary
    if "Friday" in temps:
        print("Friday's temperature:", temps["Friday"], "F")
    else:
        print("Friday is not in the temperature dictionary.")

    # Task 3: Use setdefault() to add "Thursday" with 70
    temps.setdefault("Thursday", 70)
    print("\nAfter setdefault('Thursday', 70):", temps)

    # Try again - should not change since Thursday now exists
    temps.setdefault("Thursday", 999)  # This should NOT overwrite
    print("After setdefault('Thursday', 999):", temps, "(unchanged!)")

    # Task 4: Demonstrate dynamic views
    print("\nDynamic View Demonstration:")
    keys_view = temps.keys()
    print("  Keys view before:", keys_view)
    temps["Friday"] = 80
    print("  Keys view after adding Friday:", keys_view)
    print("  Notice: The view object automatically updated!")
    print()
    return temps


# ----- Advanced (15 pts) -----
# Given: prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
# Write code that:
# 1. Calculates the total value and average price.
# 2. Finds the most and least expensive items (both name and price).
# 3. Compares memory usage between prices.keys() and list(prices.keys()).
# 4. Uses update() to add 3 new products, then shows all products.
def exercise_2_2_advanced():
    print("=" * 50)
    print("Unit 2.2 - Advanced: Dictionary Analysis and Memory Comparison")
    print("=" * 50)

    import sys

    prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

    # Task 1: Total value and average price
    total = sum(prices.values())
    average = total / len(prices)
    print("Total value: ${}".format(total))
    print("Average price: ${:.2f}".format(average))

    # Task 2: Most and least expensive items
    most_expensive_name = max(prices, key=prices.get)
    most_expensive_price = prices[most_expensive_name]
    least_expensive_name = min(prices, key=prices.get)
    least_expensive_price = prices[least_expensive_name]

    print("\nMost expensive: {} at ${}".format(most_expensive_name, most_expensive_price))
    print("Least expensive: {} at ${}".format(least_expensive_name, least_expensive_price))

    # Task 3: Memory usage comparison
    keys_view = prices.keys()
    keys_list = list(prices.keys())
    view_size = sys.getsizeof(keys_view)
    list_size = sys.getsizeof(keys_list)

    print("\nMemory Usage Comparison:")
    print("  keys() view size:     {} bytes".format(view_size))
    print("  list(keys()) size:    {} bytes".format(list_size))
    print("  The view is {} bytes smaller (constant vs proportional)".format(list_size - view_size))

    # Task 4: Use update() to add 3 new products
    new_products = {"monitor": 299, "keyboard": 79, "mouse": 29}
    prices.update(new_products)
    print("\nAfter update() with new products:")
    for product, price in prices.items():
        print("  {}: ${}".format(product, price))
    print()
    return prices


# ============================================================
# UNIT 2.3: The items() Method
# ============================================================

# ----- Beginner (5 pts) -----
# Given: colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
# 1. Use a loop with .items() to print each fruit and its color:
#    "The apple is red", "The banana is yellow", "The grape is purple"
# 2. Without running the code, predict what list(colors.items()) returns.
def exercise_2_3_beginner():
    print("=" * 50)
    print("Unit 2.3 - Beginner: Iterating with items()")
    print("=" * 50)

    colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

    # Task 1: Loop with .items()
    print("Fruit colors:")
    for fruit, color in colors.items():
        print("  The {} is {}".format(fruit, color))

    # Task 2: Predict list(colors.items())
    print("\nPrediction for list(colors.items()):")
    print("  It returns a list of tuples: [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple')]")
    print("  Actual result:", list(colors.items()))
    print()
    return colors


# ----- Intermediate (10 pts) -----
# Given: prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
# 1. Write a loop using items() that prints each item with 10% tax added.
# 2. Count how many items cost more than $4.00 using iteration.
# 3. Use tuple unpacking to swap two variables x=10 and y=20 in one line.
# 4. Given a list [1, 2, 3, 4, 5], use extended unpacking to get the first 
#    element, last element, and middle elements separately.
def exercise_2_3_intermediate():
    print("=" * 50)
    print("Unit 2.3 - Intermediate: items() Loop, Counting, and Unpacking")
    print("=" * 50)

    # Task 1: Print each item with 10% tax
    prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
    print("Prices with 10% tax:")
    for item, price in prices.items():
        price_with_tax = price * 1.10
        print("  {}: ${:.2f} + tax = ${:.2f}".format(item, price, price_with_tax))

    # Task 2: Count items over $4.00
    count_over_4 = 0
    for price in prices.values():
        if price > 4.00:
            count_over_4 += 1
    print("\nNumber of items costing more than $4.00:", count_over_4)

    # Task 3: Swap variables using tuple unpacking
    x, y = 10, 20
    print("\nBefore swap: x = {}, y = {}".format(x, y))
    x, y = y, x
    print("After swap:  x = {}, y = {}".format(x, y))

    # Task 4: Extended unpacking
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print("\nExtended unpacking of {}:".format(numbers))
    print("  first =", first)
    print("  middle =", middle)
    print("  last =", last)
    print()
    return prices


# ----- Advanced (15 pts) -----
# Given: scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
# 1. Use items() with the max() function and a lambda to find the student 
#    with the highest score.
# 2. Create two new dictionaries: passed (grade >= 70) and failed (grade < 70) 
#    using iteration.
# 3. Calculate the class average and create a dictionary showing each student's 
#    deviation from the average.
# 4. Write a performance test comparing items() iteration vs keys() with lookup 
#    for a dictionary with 50,000 entries.
def exercise_2_3_advanced():
    print("=" * 50)
    print("Unit 2.3 - Advanced: items() Analysis and Performance Test")
    print("=" * 50)

    import time

    scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

    # Task 1: Find highest score using max() with lambda
    best_student, best_score = max(scores.items(), key=lambda x: x[1])
    print("Highest score: {} with {}".format(best_student, best_score))

    # Task 2: Create passed and failed dictionaries
    passed = {}
    failed = {}
    for name, grade in scores.items():
        if grade >= 70:
            passed[name] = grade
        else:
            failed[name] = grade
    print("\nPassed (>= 70):", passed)
    print("Failed (< 70): ", failed)

    # Task 3: Calculate average and deviation dictionary
    average = sum(scores.values()) / len(scores)
    deviations = {}
    for name, grade in scores.items():
        deviations[name] = grade - average
    print("\nClass average: {:.1f}".format(average))
    print("Deviations from average:")
    for name, dev in deviations.items():
        sign = "+" if dev >= 0 else ""
        print("  {}: {}{:.1f}".format(name, sign, dev))

    # Task 4: Performance test - items() vs keys() + lookup
    print("\nPerformance Test (50,000 entries):")
    big_dict = {i: i * 2 for i in range(50000)}

    # Method 1: items() iteration
    start = time.time()
    total_items = 0
    for k, v in big_dict.items():
        total_items += k + v
    items_time = time.time() - start

    # Method 2: keys() + lookup
    start = time.time()
    total_keys = 0
    for k in big_dict.keys():
        v = big_dict[k]
        total_keys += k + v
    keys_time = time.time() - start

    print("  items() iteration:     {:.6f} seconds".format(items_time))
    print("  keys() + lookup:       {:.6f} seconds".format(keys_time))
    if items_time > 0:
        print("  items() is {:.1f}x faster than keys() + lookup".format(keys_time / items_time))
    print()
    return scores


# ============================================================
# MAIN / TEST DRIVER
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("CS1350 HW2: Dictionaries Basics")
    print("=" * 60)
    print()

    # Unit 1.1
    exercise_1_1_beginner()
    exercise_1_1_intermediate()
    exercise_1_1_advanced()

    # Unit 1.2
    exercise_1_2_beginner()
    exercise_1_2_intermediate()
    exercise_1_2_advanced()

    # Unit 1.3
    exercise_1_3_beginner()
    exercise_1_3_intermediate()
    exercise_1_3_advanced()

    # Unit 2.1
    exercise_2_1_beginner()
    exercise_2_1_intermediate()
    exercise_2_1_advanced()

    # Unit 2.2
    exercise_2_2_beginner()
    exercise_2_2_intermediate()
    exercise_2_2_advanced()

    # Unit 2.3
    exercise_2_3_beginner()
    exercise_2_3_intermediate()
    exercise_2_3_advanced()

    print("=" * 60)
    print("All exercises completed!")
    print("=" * 60)