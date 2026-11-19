"""
CS1350AA Midterm - Part II: Coding  (ANNOTATED STUDY VERSION)

"""

import json
from abc import ABC, abstractmethod


# =============================================================================
# Problem 1: Course Gradebook (Dictionaries)
# =============================================================================
class Gradebook:
    def __init__(self):
        # >> Runs when you write Gradebook(). "self" is the new object.
        # >> self.grades is an empty dict that will hold {student: {assignment: score}}.
        self.grades = {}

    def add_score(self, student, assignment, score):
        # >> STEP 1: Is this a new student? If so, give them an empty inner dict.
        # >>         Without this, the line below would raise KeyError.
        if student not in self.grades:
            self.grades[student] = {}
        # >> STEP 2: Assign into the inner dict. If the assignment already exists,
        # >>         this REPLACES the old score. That is the "overwrite" rule.
        self.grades[student][assignment] = score  # overwrites if it exists

    def student_average(self, student):
        # >> STEP 1: .get() returns None for unknown students instead of KeyError.
        scores = self.grades.get(student)
        # >> STEP 2: "not scores" is True for None (no student) AND {} (no scores).
        if not scores:
            return None
        # >> STEP 3: sum of the score values / number of scores.
        # >>         Alice: (90 + 80) / 2 = 85.0
        return sum(scores.values()) / len(scores)

    def assignment_average(self, assignment):
        # >> STEP 1: Loop over each student's inner dict (called s).
        # >>         Keep s[assignment] only if that student has it.
        # >>         For "hw1" -> [90, 70, 100]. For "hw9" -> [] (empty).
        scores = [s[assignment] for s in self.grades.values() if assignment in s]
        # >> STEP 2: Empty list is falsy, so nobody has this assignment -> None.
        if not scores:
            return None
        # >> STEP 3: 260 / 3 = 86.666...
        return sum(scores) / len(scores)

    def top_students(self, n):
        # >> sorted(self.grades) loops over the dict KEYS (the names).
        # >> key=lambda name: ... tells sorted to rank each name by that student's
        # >> average, not alphabetically. reverse=True = highest first.
        # >> Averages: Carol 100, Alice 85, Bob 72.5.
        ranked = sorted(self.grades, key=lambda name: self.student_average(name), reverse=True)
        # >> [:n] keeps only the first n names.
        return ranked[:n]

    def missing(self, assignment):
        # >> .items() gives (name, inner_dict) pairs.
        # >> Keep names whose inner dict does NOT contain the assignment,
        # >> then sorted() puts them in alphabetical order.
        return sorted(name for name, s in self.grades.items() if assignment not in s)


def run_problem_1():
    print("=== Problem 1: Gradebook ===")
    gb = Gradebook()
    gb.add_score("Alice", "hw1", 90)
    gb.add_score("Alice", "hw2", 80)
    gb.add_score("Bob", "hw1", 70)
    gb.add_score("Bob", "hw2", 60)
    gb.add_score("Carol", "hw1", 100)
    gb.add_score("Bob", "hw2", 75)  # overwrite  >> Bob's hw2 changes 60 -> 75

    print(gb.student_average("Alice"))     # 85.0
    print(gb.student_average("Bob"))       # 72.5   (70 + 75) / 2
    print(gb.student_average("Zed"))       # None   (not in the gradebook)
    print(gb.assignment_average("hw1"))    # 86.66666666666667
    print(gb.assignment_average("hw9"))    # None   (nobody has hw9)
    print(gb.top_students(2))              # ['Carol', 'Alice']
    print(gb.missing("hw2"))               # ['Carol']  (Carol has no hw2)


# =============================================================================
# Problem 2: Access Control with Sets
# =============================================================================
class Door:
    def __init__(self, name):
        # >> Each Door has a name and its OWN empty set of authorized card IDs.
        self.name = name
        self.cards = set()

    def grant(self, card_id):
        # >> .add() puts the card in the set. Duplicates are ignored automatically.
        self.cards.add(card_id)

    def revoke(self, card_id):
        # >> discard() does NOTHING if the card is missing. remove() would raise
        # >> KeyError, which is why discard is the right choice here.
        self.cards.discard(card_id)  # no error if absent

    def can_open(self, card_id):
        # >> "in" on a set returns True/False, and is very fast.
        return card_id in self.cards


def master_cards(doors):
    # >> Cards that open EVERY door = intersection of all the doors' sets.
    # >> STEP 1: Guard for an empty list.
    if not doors:
        return set()
    # >> STEP 2: Start with a COPY of the first door's cards. The copy matters:
    # >>         &= changes a set in place, so without set(...) you would wipe out
    # >>         the first door's real cards.
    result = set(doors[0].cards)
    # >> STEP 3: Intersect with each remaining door.
    # >>         {101,102,103,104} & {101,103} = {101,103}; & {101,105} = {101}
    for door in doors[1:]:
        result &= door.cards
    return result


def single_door_cards(doors):
    # >> STEP 1: Count how many doors each card appears on.
    counts = {}
    for door in doors:
        for card in door.cards:
            # >> .get(card, 0) = current count, or 0 if first time seen. Then +1.
            counts[card] = counts.get(card, 0) + 1
    # >> counts is now {101:3, 102:1, 103:2, 104:1, 105:1}
    # >> STEP 2: Keep cards whose count is exactly 1.
    return {card for card, n in counts.items() if n == 1}


def unused_cards(all_cards, doors):
    # >> STEP 1: Build the union of every door's cards (all cards that open
    # >>         at least one door). |= is union-update.
    used = set()
    for door in doors:
        used |= door.cards
    # >> STEP 2: Set difference. Cards in all_cards but NOT in used.
    # >>         {101,102,105,200} - {101,102,103,104,105} = {200}
    return set(all_cards) - used


def audit(doors):
    # >> Print each door's name and how many cards it has, then the master cards.
    for door in doors:
        print(f"{door.name}: {len(door.cards)} cards")
    print(f"Master cards: {master_cards(doors)}")


def run_problem_2():
    print("\n=== Problem 2: Access Control ===")
    lobby = Door("Lobby")
    for c in [101, 102, 103, 104]:
        lobby.grant(c)
    lab = Door("Lab")
    for c in [101, 103, 105]:
        lab.grant(c)
    server = Door("Server Room")
    for c in [101, 105]:
        server.grant(c)

    lab.revoke(105)    # >> Lab loses 105, so Lab = {101, 103}
    lab.revoke(999)  # no error  >> discard ignores missing items
    print(lab.can_open(103), lab.can_open(105))  # True False

    doors = [lobby, lab, server]
    print(master_cards(doors))                           # {101}
    # NOTE: the exam comment says {102, 104}, but the real output is
    # {102, 104, 105}: after the revoke, 105 is only on the Server Room.
    print(single_door_cards(doors))                      # {102, 104}  (exam's comment)
    print(unused_cards({101, 102, 105, 200}, doors))     # {200}
    audit(doors)


# =============================================================================
# Problem 3: Sensor Log Processor (File Processing)
# =============================================================================
def process_readings(in_file, json_file, alert_file, limit):
    """
    Summarize sensor readings into a JSON file and write alerts.

    Returns:
        number of alert lines written
    """
    # >> stats keeps RUNNING TOTALS per sensor (not every reading), so memory
    # >> use stays small even for huge files.
    stats = {}          # sensor_id -> {"count", "total", "max"}
    alert_lines = []    # alert strings to write at the end

    # >> "with" closes the file automatically, even if an error happens.
    with open(in_file, "r") as f:
        # >> Reads ONE line at a time.
        for line in f:
            # >> strip() removes the trailing "\n". A blank line becomes "".
            line = line.strip()
            # >> "" is falsy, so blank lines are skipped. Without this, split
            # >> would return 1 piece and the 3-way unpacking would crash.
            if not line:
                continue
            # >> "08:10,temp1,26.0" -> timestamp="08:10", sensor_id="temp1", value_str="26.0"
            timestamp, sensor_id, value_str = line.split(",")
            # >> The file holds text, so convert to a number for math/comparison.
            value = float(value_str)

            # >> First time we see this sensor: create its record.
            # >> max starts at the first value (not 0) so negatives work too.
            if sensor_id not in stats:
                stats[sensor_id] = {"count": 0, "total": 0.0, "max": value}
            # >> s is NOT a copy. It points at the same inner dict inside stats.
            s = stats[sensor_id]
            s["count"] += 1
            s["total"] += value
            if value > s["max"]:
                s["max"] = value

            # >> Alert if strictly greater than limit. We write value_str (the
            # >> original text) so the output matches the input exactly ("26.0").
            if value > limit:
                alert_lines.append(f"{timestamp} {sensor_id} {value_str}")

    # >> Turn running totals into the required output.  average = total / count.
    summary = {
        sensor: {
            "count": s["count"],
            "average": s["total"] / s["count"],
            "max": s["max"],
        }
        for sensor, s in stats.items()
    }

    # >> "w" creates or overwrites. json.dump writes to a FILE OBJECT
    # >> (json.dumps would return a string). indent=2 = pretty-print.
    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)

    # >> One alert per line; we add "\n" ourselves because write() doesn't.
    with open(alert_file, "w") as f:
        for line in alert_lines:
            f.write(line + "\n")

    # >> Number of alerts written.
    return len(alert_lines)


def run_problem_3():
    print("\n=== Problem 3: Sensor Log Processor ===")
    # >> Create the input file (note the blank line in the middle on purpose).
    with open("readings.txt", "w") as f:
        f.write("08:00,temp1,21.5\n")
        f.write("08:00,temp2,19.0\n")
        f.write("\n")
        f.write("08:10,temp1,26.0\n")
        f.write("08:10,temp2,18.5\n")
        f.write("08:20,temp1,24.5\n")

    alerts = process_readings("readings.txt", "summary.json", "alerts.txt", 24.0)
    print(alerts)  # 2   >> 26.0 and 24.5 are both > 24.0

    with open("summary.json", "r") as f:
        summary = json.load(f)  # >> json.load reads from a file object
    print(summary["temp1"])  # {'count': 3, 'average': 24.0, 'max': 26.0}
    print(summary["temp2"])  # {'count': 2, 'average': 18.75, 'max': 19.0}

    with open("alerts.txt", "r") as f:
        print(f.read())
    # 08:10 temp1 26.0
    # 08:20 temp1 24.5


# =============================================================================
# Problem 4: Shipping Rates with Inheritance
# =============================================================================
class Shipment(ABC):
    # >> ABC + an @abstractmethod = abstract class. You cannot write
    # >> Shipment("X", 1); Python raises TypeError.
    def __init__(self, tracking_id, weight_kg):
        # >> Validate first, so a bad weight can never create an object.
        Shipment.validate_weight(weight_kg)
        self.tracking_id = tracking_id
        self.weight_kg = weight_kg

    @abstractmethod
    def cost(self):
        # >> No body on purpose. Every subclass MUST define its own cost().
        pass

    def label(self):
        # >> self.cost() runs the SUBCLASS's version at runtime. That is
        # >> polymorphism. :.2f = 2 decimal places.
        return f"{self.tracking_id} ({self.weight_kg} kg): ${self.cost():.2f}"

    @staticmethod
    def validate_weight(weight_kg):
        # >> @staticmethod: gets neither self nor cls. Just a utility function
        # >> that lives in the class. Called as Shipment.validate_weight(-1).
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")


class StandardShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00):
        # >> super().__init__ runs the PARENT constructor (sets + validates the
        # >> id and weight). Skip it and those attributes never exist.
        super().__init__(tracking_id, weight_kg)
        self.rate_per_kg = rate_per_kg

    def cost(self):
        # >> S100: 4.0 * 2.00 = 8.00
        return self.weight_kg * self.rate_per_kg


class ExpressShipment(StandardShipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00, surcharge=10.00):
        # >> Pass the shared fields UP to StandardShipment, keep surcharge here.
        super().__init__(tracking_id, weight_kg, rate_per_kg)
        self.surcharge = surcharge

    def cost(self):
        # >> super().cost() = StandardShipment's formula (reused, not rewritten).
        # >> E200: (2.5 * 2.00) + 10.00 = 15.00
        return super().cost() + self.surcharge


class InternationalShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, country, customs_pct=0.15):
        super().__init__(tracking_id, weight_kg)
        self.country = country
        self.customs_pct = customs_pct

    def cost(self):
        # >> I300: 3.0 * 5.00 * 1.15 = 17.25
        return self.weight_kg * 5.00 * (1 + self.customs_pct)


def manifest(shipments):
    total = 0
    for s in shipments:
        # >> No isinstance checks needed. Each object knows its own cost().
        print(s.label())
        total += s.cost()
    print(f"Total: ${total:.2f}")
    return total


def run_problem_4():
    print("\n=== Problem 4: Shipments ===")
    shipments = [
        StandardShipment("S100", 4.0),
        ExpressShipment("E200", 2.5),
        InternationalShipment("I300", 3.0, country="Canada"),
    ]
    manifest(shipments)
    # S100 (4.0 kg): $8.00
    # E200 (2.5 kg): $15.00
    # I300 (3.0 kg): $17.25
    # Total: $40.25

    try:
        Shipment.validate_weight(-1)
    except ValueError as e:
        print("Caught:", e)  # Caught: Weight must be positive


# =============================================================================
# Problem 5: Polynomial Class with Operator Overloading
# =============================================================================
class Polynomial:
    def __init__(self, coeffs):
        # >> list(...) makes a COPY so later changes to the caller's list
        # >> don't change this polynomial. Index i = coefficient of x**i.
        self.coeffs = list(coeffs)  # store a copy

    def degree(self):
        """Highest index with a non-zero coefficient (0 if all zero)."""
        # >> Count down from the top index; the first non-zero one is the degree.
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] != 0:
                return i
        return 0

    # --- Display ---
    def __str__(self):
        # >> Used by print(). Builds terms from highest power down to 0.
        terms = []
        # >> range(len-1, -1, -1) counts DOWN: e.g. 2, 1, 0
        for power in range(len(self.coeffs) - 1, -1, -1):
            c = self.coeffs[power]
            if c == 0:
                continue                       # >> skip zero terms
            if power == 0:
                terms.append(f"{c}")           # >> constant: just the number
            else:
                coef = "" if c == 1 else f"{c}"  # >> drop a coefficient of 1
                if power == 1:
                    terms.append(f"{coef}x")       # >> x, not x^1
                else:
                    terms.append(f"{coef}x^{power}")
        # >> ["3x^2", "2x", "1"] -> "3x^2 + 2x + 1"
        return " + ".join(terms)

    def __repr__(self):
        # >> For programmers (shell, repr()). print() uses __str__ instead.
        return f"Polynomial({self.coeffs})"

    # --- Container ---
    def __len__(self):
        # >> Makes len(p) work.
        return len(self.coeffs)

    def __getitem__(self, i):
        # >> Makes p[i] work. Past the end returns 0, which is what lets
        # >> __add__ handle polynomials of different lengths.
        if i < len(self.coeffs):
            return self.coeffs[i]
        return 0

    def __call__(self, x):
        # >> Makes p(2) work like a function. enumerate gives (index, coeff).
        # >> p(2) = 1*2**0 + 2*2**1 + 3*2**2 = 1 + 4 + 12 = 17
        return sum(c * x ** i for i, c in enumerate(self.coeffs))

    # --- Arithmetic ---
    def __add__(self, other):
        # >> Use the longer length; the shorter one supplies 0s via __getitem__.
        # >> [1,2,3] + [0,1] -> [1+0, 2+1, 3+0] = [1,3,3]. Returns a NEW object.
        n = max(len(self), len(other))
        return Polynomial([self[i] + other[i] for i in range(n)])

    def __mul__(self, scalar):
        # >> Scalar multiply: every coefficient times the number.
        return Polynomial([c * scalar for c in self.coeffs])

    # --- Comparison (by degree) ---
    def __eq__(self, other):
        # >> Equal if the highest non-zero positions match. [1,2,3] and [5,0,1]
        # >> are both degree 2, so they are "equal" under this exam's rule.
        return self.degree() == other.degree()

    def __lt__(self, other):
        # >> Less than if the degree is smaller. q (degree 1) < p (degree 2).
        return self.degree() < other.degree()


def run_problem_5():
    print("\n=== Problem 5: Polynomial ===")
    p = Polynomial([1, 2, 3])  # 1 + 2x + 3x^2
    q = Polynomial([0, 1])     # x

    print(p)                          # 3x^2 + 2x + 1
    print(q)                          # x
    print(repr(p))                    # Polynomial([1, 2, 3])
    print(len(p))                     # 3
    print(p[2], p[7])                 # 3 0
    print(p(2))                       # 17
    print(q(5))                       # 5
    r = p + q
    print(r)                          # 3x^2 + 3x + 1
    print(p * 2)                      # 6x^2 + 4x + 2
    print(p == Polynomial([5, 0, 1])) # True
    print(q < p)                      # True


# =============================================================================
# Run everything
# =============================================================================
if __name__ == "__main__":
    # >> Runs only when you execute THIS file directly (not when imported).
    run_problem_1()
    run_problem_2()
    run_problem_3()
    run_problem_4()
    run_problem_5()