"""
HW4: Dictionary Advanced and Set - Solutions
CS1350 Computer Science II
Covers Week 2 Lecture 1 (Dictionary III) and Week 2 Lecture 2 (Set)
"""

import time


def separator(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ============================================================
# Week 2 Lecture 1 - Dictionary III
# Unit 3.1: Iterating Through Dictionaries
# ============================================================
def unit_3_1():
    separator("Unit 3.1 Practice Exercises")

    # Beginner
    print("\n-- Beginner --")
    inventory = {"apples": 50, "bananas": 30, "oranges": 25}
    # 1. Print each product name using default iteration (keys)
    for product in inventory:
        print(product)
    # 2. Calculate total items using values()
    total_items = sum(inventory.values())
    print("Total items:", total_items)
    # 3. Print each product with quantity using items()
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")

    # Intermediate
    print("\n-- Intermediate --")
    prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
    # 1. Print products sorted alphabetically
    for product in sorted(prices):
        print(f"{product}: {prices[product]}")
    # 2. Print products sorted by price (cheapest first)
    for product in sorted(prices, key=prices.get):
        print(f"{product}: {prices[product]}")
    # 3. Find and print the most expensive item using items()
    most_expensive, highest_price = max(prices.items(), key=lambda item: item[1])
    print(f"Most expensive: {most_expensive} at ${highest_price}")

    # Advanced
    print("\n-- Advanced --")
    temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}
    # 1. Calculate average temperature using values()
    avg_temp = sum(temps.values()) / len(temps)
    print(f"Average temperature: {avg_temp:.2f}")
    # 2. Find the hottest and coldest days in a single loop
    hottest_day = coldest_day = None
    hottest_temp = float("-inf")
    coldest_temp = float("inf")
    for day, temp in temps.items():
        if temp > hottest_temp:
            hottest_temp = temp
            hottest_day = day
        if temp < coldest_temp:
            coldest_temp = temp
            coldest_day = day
    print(f"Hottest: {hottest_day} ({hottest_temp}F)")
    print(f"Coldest: {coldest_day} ({coldest_temp}F)")
    # 3. Count how many days were above the average
    above_avg = sum(1 for temp in temps.values() if temp > avg_temp)
    print(f"Days above average: {above_avg}")


# ============================================================
# Unit 3.2: Advanced Iteration & Nested Dictionaries
# ============================================================
def unit_3_2():
    separator("Unit 3.2 Practice Exercises")

    # Beginner
    print("\n-- Beginner --")
    products = {"laptop": {"price": 999, "stock": 15},
                "phone": {"price": 699, "stock": 50}}
    # 1. Print the laptop's price
    print("Laptop price:", products["laptop"]["price"])
    # 2. Print each product with its stock
    for product, details in products.items():
        print(f"{product}: {details['stock']} in stock")

    # Intermediate
    print("\n-- Intermediate --")
    # 1. Create a dictionary from two lists using zip()
    countries = ["USA", "Canada", "Mexico"]
    capitals = ["Washington", "Ottawa", "Mexico City"]
    country_capitals = dict(zip(countries, capitals))
    print(country_capitals)
    # 2. Add a new product
    products["tablet"] = {"price": 449, "stock": 30}
    print(products)
    # 3. Safely remove all products with stock < 20
    for name in list(products.keys()):
        if products[name]["stock"] < 20:
            del products[name]
    print("After removing low stock:", products)

    # Advanced
    print("\n-- Advanced --")
    company = {"Engineering": {"Alice": 95000, "Bob": 85000},
               "Marketing": {"Carol": 75000, "Dave": 70000}}
    # 1. Print all employees with their salaries (nested iteration)
    for department, employees in company.items():
        print(f"\n{department}:")
        for name, salary in employees.items():
            print(f"  {name}: ${salary:,}")
    # 2. Calculate the average salary per department
    for department, employees in company.items():
        avg = sum(employees.values()) / len(employees)
        print(f"{department} average salary: ${avg:,.2f}")
    # 3. Find the highest-paid employee across all departments
    best_dept = best_name = None
    best_salary = float("-inf")
    for department, employees in company.items():
        for name, salary in employees.items():
            if salary > best_salary:
                best_salary = salary
                best_dept = department
                best_name = name
    print(f"Highest paid: {best_name} in {best_dept} with ${best_salary:,}")


# ============================================================
# Unit 3.3: Dictionary Patterns & Transformations
# ============================================================
def unit_3_3():
    separator("Unit 3.3 Practice Exercises")

    # Beginner
    print("\n-- Beginner --")
    # 1. Comprehension mapping numbers 1-5 to their cubes
    cubes = {x: x**3 for x in range(1, 6)}
    print("Cubes:", cubes)
    # 2. Convert temps to Celsius
    temps = {"Mon": 72, "Tue": 68, "Wed": 75}
    temps_c = {day: round((f - 32) * 5 / 9, 1) for day, f in temps.items()}
    print("Temps in Celsius:", temps_c)

    # Intermediate
    print("\n-- Intermediate --")
    scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
    student_ids = {"Alice": 101, "Bob": 102}
    # 1. Dict with only scores >= 70
    passing = {name: score for name, score in scores.items() if score >= 70}
    print("Passing:", passing)

    # 2. Dict converting scores to letter grades
    def to_letter(s):
        if s >= 90:
            return "A"
        if s >= 80:
            return "B"
        if s >= 70:
            return "C"
        return "F"

    letter_grades = {name: to_letter(score) for name, score in scores.items()}
    print("Letter grades:", letter_grades)

    # 3. Invert student_ids to look up by ID
    id_lookup = {sid: name for name, sid in student_ids.items()}
    print("Lookup by ID:", id_lookup)

    # Advanced
    print("\n-- Advanced --")
    sales = [("North", "Alice", 5000), ("South", "Bob", 4500),
             ("North", "Carol", 6000), ("South", "Alice", 3500)]
    # 1. Total sales by region
    by_region = {}
    for region, person, amount in sales:
        by_region[region] = by_region.get(region, 0) + amount
    print("Sales by region:", by_region)

    # 2. Total sales by salesperson
    by_person = {}
    for region, person, amount in sales:
        by_person[person] = by_person.get(person, 0) + amount
    print("Sales by person:", by_person)

    # 3. Nested dict {region: {person: total}}
    nested = {}
    for region, person, amount in sales:
        nested.setdefault(region, {})
        nested[region][person] = nested[region].get(person, 0) + amount
    print("Nested sales:", nested)


# ============================================================
# Week 2 Lecture 2 - Sets
# Unit 1: Set Theory and Python Sets
# ============================================================
def set_unit_1():
    separator("Set Unit 1 Practice Exercises")

    # Beginner
    print("\n-- Beginner --")
    # 1. Set of vowels
    vowels = {"a", "e", "i", "o", "u"}
    print("Vowels:", vowels)
    # 2. Set from list with duplicates + count
    numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
    print("Unique numbers:", numbers, "| count:", len(numbers))
    # 3. What's wrong: empty = {} creates an empty DICTIONARY
    empty_dict = {}
    empty_set = set()
    print(type(empty_dict), type(empty_set))

    # Intermediate
    print("\n-- Intermediate --")
    # 1. Unique characters in "mississippi"
    text = "mississippi"
    unique_chars = set(text)
    print("Unique chars:", unique_chars, "| count:", len(unique_chars))
    # 2. Remove duplicates from emails, convert back to list
    emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
    unique_emails = list(set(emails))
    print("Unique emails:", unique_emails)
    # 3. Why s = {[1,2],[3,4]} fails: lists are mutable/unhashable
    s = {(1, 2), (3, 4)}  # fixed version using tuples
    print("Fixed set of tuples:", s)

    # Advanced
    print("\n-- Advanced --")
    # 1. Time set membership vs list membership (1,000,000 items)
    big_set = set(range(1_000_000))
    big_list = list(range(1_000_000))

    start = time.perf_counter()
    _ = 999_999 in big_set
    set_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = 999_999 in big_list
    list_time = time.perf_counter() - start

    print(f"Set lookup:  {set_time:.6f}s")
    print(f"List lookup: {list_time:.6f}s")
    print(f"Set is ~{list_time / set_time:.0f}x faster")

    # 2. Frozenset as a dictionary key
    fs = frozenset([1, 2, 3])
    d = {fs: "frozen!"}
    print("Frozenset key:", d)

    # 3. Unique nodes from graph edges
    edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
    nodes = set()
    for a, b in edges:
        nodes.add(a)
        nodes.add(b)
    print("Unique nodes:", nodes)


# ============================================================
# Unit 2: Set Operations
# ============================================================
def set_unit_2():
    separator("Set Unit 2 Practice Exercises")

    # Beginner
    print("\n-- Beginner --")
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Only in a:", a - b)

    # Intermediate
    print("\n-- Intermediate --")
    morning = {"Alice", "Bob", "Carol"}
    evening = {"Carol", "Dave", "Eve"}
    weekend = {"Alice", "Eve", "Frank"}
    # 1. Work ALL shifts
    print("All shifts:", morning & evening & weekend)
    # 2. Work at least one shift
    print("Any shift:", morning | evening | weekend)
    # 3. ONLY work morning
    print("Morning only:", morning - evening - weekend)
    # 4. Work exactly one shift
    exactly_one = (morning ^ evening ^ weekend) - (morning & evening & weekend)
    print("Exactly one shift:", exactly_one)

    # Advanced
    print("\n-- Advanced --")
    prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
    has_space = {"Bob", "Carol", "Eve", "Frank"}
    paid_tuition = {"Alice", "Carol", "Eve"}
    all_students = prereqs_met | has_space | paid_tuition
    # 1. Eligible = meet ALL three criteria
    print("Eligible:", prereqs_met & has_space & paid_tuition)
    # 2. Met prereqs but haven't paid
    print("Met prereqs, not paid:", prereqs_met - paid_tuition)
    # 3. Missing prereqs OR tuition = everyone except those with both
    print("Need prereqs or tuition:", all_students - (prereqs_met & paid_tuition))


# ============================================================
# Unit 3: Set Methods, Comprehensions & Patterns
# ============================================================
def find_duplicates(lst):
    """Return a set of elements that appear more than once."""
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return {item for item, count in counts.items() if count > 1}


def common_chars(s1, s2):
    """Return the set of characters common to both strings."""
    return set(s1) & set(s2)


def set_unit_3():
    separator("Set Unit 3 Practice Exercises")

    # Beginner
    print("\n-- Beginner --")
    # 1. Create {1,2,3}, add 4, remove 1
    s = {1, 2, 3}
    s.add(4)
    s.remove(1)
    print("After add/remove:", s)
    # 2. Set comprehension of evens 0-20
    evens = {x for x in range(21) if x % 2 == 0}
    print("Evens 0-20:", evens)
    # 3. discard() is safe; remove() raises KeyError on missing element
    s.discard(99)   # no error, nothing happens
    print("After discard(99):", s)
    try:
        s.remove(99)  # KeyError!
    except KeyError as e:
        print("remove(99) raised KeyError:", e)

    # Intermediate
    print("\n-- Intermediate --")
    # 1. Remove duplicates while preserving order
    data = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
    seen = set()
    unique_ordered = []
    for x in data:
        if x not in seen:
            seen.add(x)
            unique_ordered.append(x)
    print("Ordered unique:", unique_ordered)

    # 2. Unique words from sentence (lowercased)
    sentence = "To be or not to be that is the question"
    words = {w.lower() for w in sentence.split()}
    print("Unique words:", words)

    # 3. Find missing numbers
    expected = set(range(1, 11))
    actual = {1, 2, 4, 5, 7, 8, 10}
    print("Missing:", expected - actual)

    # Advanced
    print("\n-- Advanced --")
    # 1. find_duplicates()
    print("Duplicates:", find_duplicates([1, 2, 2, 3, 3, 3, 4]))

    # 2. Employee skill analysis
    alice = {"Python", "SQL", "Excel", "Tableau"}
    bob = {"Python", "Java", "SQL", "AWS"}
    carol = {"Python", "R", "SQL", "Tableau"}
    print("All three have:", alice & bob & carol)
    print("Only Alice:", alice - bob - carol)
    print("All team skills:", alice | bob | carol)

    # 3. Common characters
    print("Common chars:", common_chars("hello", "world"))


if __name__ == "__main__":
    unit_3_1()
    unit_3_2()
    unit_3_3()
    set_unit_1()
    set_unit_2()
    set_unit_3()