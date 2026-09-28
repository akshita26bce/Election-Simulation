# Election Simulation

A simple command-line election simulation program developed for a first-year college Python Essentials course.

---

## Project Description

The **Election Simulation** project is an interactive terminal-based application that simulates a basic single-choice plurality election. It allows an administrator to set up an election, add candidate names, register voter IDs, and record votes. The system ensures that only registered voters can vote, strictly enforces that each voter votes at most once, calculates current and final results, detects single winners and ties, and displays voter turnout statistics.

This program is designed strictly as an educational simulation. It does not represent a real election system and does not use real political candidates, parties, or voter records.

---

## Features

* **Election Setup**: Configure the election title, input candidates, and register voter IDs.
* **Candidate Management**: Add unique candidate names before voting begins.
* **Voter Registration**: Register unique alphanumeric voter IDs in an in-memory set.
* **Secure Voting**: Prevents unregistered voters from voting and prevents voters from casting more than one vote.
* **Accurate Vote Counting**: Real-time vote tallying using a Python dictionary.
* **Winner & Tie Determination**: Identifies the candidate with the highest vote tally, correctly reporting ties when multiple candidates share the lead.
* **Voting Statistics**: Computes turnout percentages, unvoted voter counts, and audits vote counts using Python's standard `array` module.
* **Menu-Driven Interface**: Clear, loop-based command-line interface.

---

## Concepts Used

This project strictly utilizes concepts taught in the **Python Essentials** beginner syllabus:

1. **Python Fundamentals**: Variables, student-level comments, clean indentation, and PEP 8 style naming.
2. **Input and Output Operations**: `input()` for reading terminal inputs and `print()` for formatted tables and menus.
3. **Arithmetic Operators**: `+`, `-`, `*`, `/` used in calculating vote totals, remaining unvoted counts, and turnout percentages.
4. **Assignment Operators**: `=`, `+=` for tallying votes and updating counters.
5. **Relational Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=` for menu bounds, finding max votes, and tie detection.
6. **Logical Operators**: `and`, `or`, `not` used when validating voter eligibility and menu options.
7. **Membership Operators**: `in` and `not in` for checking candidate names and voter IDs.
8. **Identity Operators**: `is` and `is not` for sentinel checks against `None` (e.g., checking if candidate roster is locked or if winner calculation is empty).
9. **Bitwise Operators**: `&` (AND) and `|` (OR) used for tracking election stage flags (`FLAG_SETUP = 1`, `FLAG_VOTING = 2`, `FLAG_CLOSED = 4`).
10. **Type Conversion & `type()`**: `int()` and `str()` for converting user inputs; `type()` used for asserting data structures.
11. **Operator Precedence**: Natural mathematical grouping, e.g., `(part / whole) * 100`.
12. **Lists**: `candidates = []` and `winners = []` for ordered collections.
13. **Tuples**: `election_info = (title, system)` for fixed election metadata, and `(winners, max_votes)` return values.
14. **Sets**: `registered_voters` and `voted_voters` for unique voter IDs and fast $O(1)$ membership checks.
15. **Dictionaries**: `votes = {candidate: count}` for mapping candidates to their vote tallies.
16. **Frozen Sets**: `locked_candidates = frozenset(candidates)` to lock candidate names once voting begins.
17. **Control-Flow**: `if`-`elif`-`else`, `for`, `while`, `break`, and `continue`.
18. **Functions**: Modular functions in `utils.py` and `main.py` with explicit parameters and return values.
19. **Modules**: Multi-file architecture using standard Python `import`.
20. **Array Data Structure**: Python's standard `array('i', ...)` module to store numerical vote counts for audit verification.
21. **Object-Oriented Programming**: `class Election` with constructor `__init__`, state attributes, and business methods.

---

## Requirements

* **Python 3.6+** (Standard installation)
* No external libraries or third-party packages are required.

---

## Installation / Setup

1. Clone or download the repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Open your command prompt / terminal and navigate to the project directory:
   ```bash
   cd election_simulation
   ```
3. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
4. Run the program using:
   ```bash
   python main.py
   ```

---

## How to Use

When the program starts, the main menu is displayed:

```text
========================================
       ELECTION SIMULATION SYSTEM       
========================================
1. Setup Election
2. Add Candidates
3. Register Voters
4. Cast Votes
5. View Current Results
6. Display Election Statistics
7. Exit
========================================
```

### Typical Workflow:
1. **Option 1 (Setup Election)**: Enter the election title, how many candidates to add, and initial voter IDs.
2. **Option 2 (Add Candidates)**: Add any additional candidates before voting commences.
3. **Option 3 (Register Voters)**: Add additional voter IDs to the registered set.
4. **Option 4 (Cast Votes)**: Enter a registered voter ID and select a candidate by number. Once the first vote is cast, candidate additions are locked.
5. **Option 5 (View Current Results)**: See current vote counts per candidate.
6. **Option 6 (Display Election Statistics)**: View voter turnout, unvoted voter count, audit sum from array, and current winner or tie.
7. **Option 7 (Exit)**: Concludes voting and displays final results before closing the program.

---

## Example Interaction

```text
========================================
       ELECTION SIMULATION SYSTEM       
========================================
1. Setup Election
2. Add Candidates
3. Register Voters
4. Cast Votes
5. View Current Results
6. Display Election Statistics
7. Exit
========================================
Enter your choice (1-7): 4

--- Cast Votes ---
Enter your Voter ID: V101

Candidates:
1. Alice
2. Bob
Select a candidate (1 to 2): 1
Vote successfully recorded for Alice!

========================================
       ELECTION SIMULATION SYSTEM       
========================================
1. Setup Election
2. Add Candidates
3. Register Voters
4. Cast Votes
5. View Current Results
6. Display Election Statistics
7. Exit
========================================
Enter your choice (1-7): 5

----------- ELECTION RESULTS -----------
Alice : 1 vote
Bob : 0 votes

Total Votes : 1
----------------------------------------
```

---

## Project Structure

```text
election_simulation/
│
├── main.py                # Command-line menu interface and user input handling
├── election.py            # Election class containing election state and business methods
├── utils.py               # Helper functions (validation without exceptions, array tally, bitwise flags)
├── README.md              # Project documentation
└── tests/
    └── test_project.py    # Test suite using plain Python assert statements
```

* **`election.py`**: Encapsulates the `Election` class, candidate list, registered and voted voter sets, vote dictionary, and methods for vote recording, winner calculation, and statistics.
* **`utils.py`**: Contains helper functions for number validation (`.isdigit()`), percentage computation, bitwise stage management (`FLAG_SETUP`, `FLAG_VOTING`, `FLAG_CLOSED`), and standard `array` vote tally auditing.
* **`main.py`**: Runs the interactive console loop and processes user menu choices.
* **`tests/test_project.py`**: Automated test script validating all election scenarios using plain `assert` statements.

---

## Running the Tests

To run the automated tests using plain Python `assert` statements (no third-party test runners needed):

```bash
python tests/test_project.py
```

Expected output:
```text
========================================
   RUNNING ELECTION SIMULATION TESTS    
========================================
Running: test_candidate_management...
  -> Passed!
Running: test_voter_registration...
  -> Passed!
Running: test_normal_voting_flow (Test 1)...
  -> Passed!
Running: test_prevent_double_voting (Test 2)...
  -> Passed!
Running: test_unregistered_voter (Test 3)...
  -> Passed!
Running: test_invalid_candidate_selection (Test 4)...
  -> Passed!
Running: test_tie_handling (Test 5)...
  -> Passed!
Running: test_no_votes_cast (Test 6)...
  -> Passed!
Running: test_no_registered_voters (Test 7)...
  -> Passed!
Running: test_data_structures_and_syllabus_topics...
  -> Passed!
========================================
 ALL 10 TESTS COMPLETED SUCCESSFULLY!   
========================================
```

---

## Limitations

* **Educational Simulation**: This program is intended strictly as an academic demonstration for the Python Essentials syllabus.
* **In-Memory Storage**: Election data is stored in memory during runtime and is reset when the program exits (no databases or file persistence).
* **Simplified Plurality Rule**: Simulates single-choice plurality voting only, without preferential ballots or multi-round runoff mechanisms.
