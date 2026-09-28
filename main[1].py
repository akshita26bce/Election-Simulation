"""
main.py - Entry point for the Election Simulation console application.
Provides a clean, beginner-friendly menu-driven interface strictly following
the Python Essentials syllabus without exception handling or external libraries.
"""

from election import Election
from utils import (
    FLAG_SETUP,
    FLAG_CLOSED,
    has_flag,
    set_flag,
    is_valid_positive_integer
)


def display_menu():
    """
    Displays the standard command-line menu.
    """
    print("\n========================================")
    print("       ELECTION SIMULATION SYSTEM       ")
    print("========================================")
    print("1. Setup Election")
    print("2. Add Candidates")
    print("3. Register Voters")
    print("4. Cast Votes")
    print("5. View Current Results")
    print("6. Display Election Statistics")
    print("7. Exit")
    print("========================================")


def setup_election(election):
    """
    Guides the user through initial election setup:
    title, initial candidates, and initial registered voters.
    """
    print("\n--- Setup Election ---")
    custom_title = input("Enter election title (press Enter for default): ").strip()
    if custom_title != "":
        election.title = custom_title
        election.election_info = (custom_title, "Single-Choice Plurality")

    # Input number of candidates
    num_cand_str = input("How many candidates would you like to enter? ").strip()
    if is_valid_positive_integer(num_cand_str):
        num_candidates = int(num_cand_str)
        count = 0
        while count < num_candidates:
            cand_name = input("Enter name for candidate " + str(count + 1) + ": ").strip()
            if cand_name == "":
                print("Candidate name cannot be empty. Please re-enter.")
                continue
            if cand_name in election.candidates:
                print("Candidate '" + cand_name + "' already exists. Please enter a different name.")
                continue
            election.add_candidate(cand_name)
            count += 1
        print("Successfully added " + str(count) + " candidate(s).")
    else:
        print("Invalid number of candidates. You can add candidates later using Option 2.")

    # Input number of voters to register
    num_voters_str = input("\nHow many voters would you like to register? ").strip()
    if is_valid_positive_integer(num_voters_str):
        num_voters = int(num_voters_str)
        voter_count = 0
        while voter_count < num_voters:
            voter_id = input("Enter Voter ID " + str(voter_count + 1) + ": ").strip()
            if voter_id == "":
                print("Voter ID cannot be empty. Please re-enter.")
                continue
            if voter_id in election.registered_voters:
                print("Voter ID '" + voter_id + "' is already registered. Please enter a unique ID.")
                continue
            election.register_voter(voter_id)
            voter_count += 1
        print("Successfully registered " + str(voter_count) + " voter(s).")
    else:
        print("Invalid number of voters. You can register voters later using Option 3.")

    election.status_flags = set_flag(election.status_flags, FLAG_SETUP)
    print("\nElection setup complete!")


def add_candidates_flow(election):
    """
    Allows adding candidates before voting begins.
    """
    print("\n--- Add Candidates ---")
    if election.locked_candidates is not None:
        print("Notice: Voting has already started! Candidate list is locked and cannot be modified.")
        return

    num_str = input("How many candidates do you want to add? ").strip()
    if not is_valid_positive_integer(num_str):
        print("Invalid number. Please enter a positive whole number.")
        return

    num_candidates = int(num_str)
    added = 0
    for i in range(num_candidates):
        name = input("Enter name for candidate " + str(i + 1) + ": ").strip()
        if name == "":
            print("Candidate name cannot be empty.")
            continue
        if election.add_candidate(name):
            print("Candidate '" + name + "' added successfully.")
            added += 1
        else:
            print("Could not add candidate '" + name + "' (duplicate or invalid).")

    print("Total added in this session: " + str(added))


def register_voters_flow(election):
    """
    Allows registering additional voters.
    """
    print("\n--- Register Voters ---")
    num_str = input("How many voters do you want to register? ").strip()
    if not is_valid_positive_integer(num_str):
        print("Invalid number. Please enter a positive whole number.")
        return

    num_voters = int(num_str)
    registered = 0
    for i in range(num_voters):
        voter_id = input("Enter Voter ID " + str(i + 1) + ": ").strip()
        if voter_id == "":
            print("Voter ID cannot be empty.")
            continue
        if election.register_voter(voter_id):
            print("Voter ID '" + voter_id + "' registered successfully.")
            registered += 1
        else:
            print("Voter ID '" + voter_id + "' is already registered.")

    print("Total voters registered in this session: " + str(registered))


def cast_vote_flow(election):
    """
    Guides a registered voter through casting their vote.
    """
    print("\n--- Cast Votes ---")

    # Relational and logical validations
    if len(election.candidates) == 0:
        print("Error: No candidates available. Please add candidates before voting.")
        return

    if len(election.registered_voters) == 0:
        print("Error: No registered voters. Please register voters before voting.")
        return

    voter_id = input("Enter your Voter ID: ").strip()
    if voter_id == "":
        print("Error: Voter ID cannot be empty.")
        return

    # Check registration and duplicate voting
    if voter_id not in election.registered_voters:
        print("Access Denied: Voter ID '" + voter_id + "' is NOT registered.")
        return

    if voter_id in election.voted_voters:
        print("Access Denied: Voter ID '" + voter_id + "' has ALREADY cast a vote.")
        return

    # Display candidates with 1-based indexing
    print("\nCandidates:")
    index = 1
    for candidate in election.candidates:
        print(str(index) + ". " + candidate)
        index += 1

    choice_str = input("Select a candidate (1 to " + str(len(election.candidates)) + "): ").strip()
    if not is_valid_positive_integer(choice_str):
        print("Invalid selection: Please enter a valid number.")
        return

    choice_num = int(choice_str)
    if choice_num < 1 or choice_num > len(election.candidates):
        print("Invalid candidate selection: Number out of range.")
        return

    selected_candidate = election.candidates[choice_num - 1]
    success, message = election.cast_vote(voter_id, selected_candidate)
    print(message)


def main():
    """
    Main application loop.
    """
    election = Election()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            setup_election(election)
        elif choice == "2":
            add_candidates_flow(election)
        elif choice == "3":
            register_voters_flow(election)
        elif choice == "4":
            cast_vote_flow(election)
        elif choice == "5":
            election.display_results()
        elif choice == "6":
            election.display_statistics()
        elif choice == "7":
            election.close_election()
            print("\nExiting Election Simulation System.")
            print("Final Results and Summary:")
            election.display_results()
            election.display_statistics()
            print("Thank you for using the Election Simulation System. Goodbye!\n")
            break
        else:
            print("Invalid option! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
