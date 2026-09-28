"""
election.py - Core election logic and data management.
Defines the Election class using lists, dictionaries, sets, tuples,
frozen sets, and arrays according to the Python Essentials syllabus.
"""

from utils import (
    FLAG_SETUP,
    FLAG_VOTING,
    FLAG_CLOSED,
    set_flag,
    has_flag,
    calculate_percentage,
    create_vote_tally_array,
    sum_tally_array
)


class Election:
    def __init__(self, title="Campus Student Council Election"):
        # Basic election title
        self.title = title

        # Tuple: Fixed election configuration metadata
        self.election_info = (self.title, "Single-Choice Plurality")

        # List: Ordered candidate names
        self.candidates = []

        # Dictionary: Mapping of candidate names to their vote counts
        self.votes = {}

        # Set: Unique registered voter IDs
        self.registered_voters = set()

        # Set: Unique voter IDs of those who have already cast a ballot
        self.voted_voters = set()

        # Frozen set: Locked snapshot of candidate names created when voting starts
        # Initialized to None to demonstrate identity comparison
        self.locked_candidates = None

        # Bitwise integer status flags (tracks lifecycle stages)
        self.status_flags = 0

    def add_candidate(self, name):
        """
        Adds a candidate to the election.
        Rejects empty names, duplicates, and additions after voting has commenced.
        """
        clean_name = name.strip()
        if clean_name == "":
            return False

        # If voting has already started, candidate roster is locked
        if self.locked_candidates is not None:
            return False

        # Check membership in candidate list
        if clean_name in self.candidates:
            return False

        self.candidates.append(clean_name)
        self.votes[clean_name] = 0
        return True

    def register_voter(self, voter_id):
        """
        Registers a new voter ID into the election.
        Rejects empty or duplicate IDs using set membership.
        """
        clean_id = voter_id.strip()
        if clean_id == "":
            return False

        # Check membership in registered voters set
        if clean_id in self.registered_voters:
            return False

        self.registered_voters.add(clean_id)
        return True

    def cast_vote(self, voter_id, candidate_name):
        """
        Casts a vote for a candidate.
        Validates registration, verifies single voting, locks candidates,
        and increments vote counts.
        """
        clean_voter_id = voter_id.strip()
        clean_candidate = candidate_name.strip()

        # Logical and membership checks
        if clean_voter_id not in self.registered_voters:
            return (False, "Voter ID '" + clean_voter_id + "' is not registered.")

        if clean_voter_id in self.voted_voters:
            return (False, "Voter ID '" + clean_voter_id + "' has already voted.")

        if clean_candidate not in self.candidates:
            return (False, "Candidate '" + clean_candidate + "' does not exist.")

        # Lock candidates into a frozen set on the first cast vote
        if self.locked_candidates is None:
            self.locked_candidates = frozenset(self.candidates)
            self.status_flags = set_flag(self.status_flags, FLAG_VOTING)

        # Update vote counts in dictionary using arithmetic assignment
        self.votes[clean_candidate] += 1

        # Add voter ID to voted voters set
        self.voted_voters.add(clean_voter_id)

        return (True, "Vote successfully recorded for " + clean_candidate + "!")

    def calculate_winner(self):
        """
        Determines the candidate or candidates with the highest number of votes.
        Returns a tuple: (winners_list, max_votes).
        Handles ties naturally by returning all candidates sharing max_votes.
        """
        if len(self.candidates) == 0:
            return (None, 0)

        # Determine the maximum votes received
        max_votes = -1
        for candidate in self.candidates:
            count = self.votes[candidate]
            if count > max_votes:
                max_votes = count

        # Collect all candidates matching the maximum vote count
        winners = []
        for candidate in self.candidates:
            if self.votes[candidate] == max_votes:
                winners.append(candidate)

        # Return result as a tuple
        return (winners, max_votes)

    def display_results(self):
        """
        Displays the current vote counts for each candidate and total votes.
        """
        print("\n----------- ELECTION RESULTS -----------")
        if len(self.candidates) == 0:
            print("No candidates registered in this election.")
            print("----------------------------------------")
            return

        total_votes = 0
        for candidate in self.candidates:
            count = self.votes[candidate]
            if count == 1:
                label = "vote"
            else:
                label = "votes"
            print(candidate + " : " + str(count) + " " + label)
            total_votes += count

        print("\nTotal Votes : " + str(total_votes))
        print("----------------------------------------")

    def display_statistics(self):
        """
        Displays comprehensive election statistics including turnout,
        unvoted voters, leader/winner, and array-based audit verification.
        """
        print("\n========= ELECTION STATISTICS =========")
        total_registered = len(self.registered_voters)
        total_votes_cast = len(self.voted_voters)
        voters_not_voted = total_registered - total_votes_cast
        total_candidates = len(self.candidates)

        # Turnout calculation using arithmetic and operator precedence
        turnout_percent = calculate_percentage(total_votes_cast, total_registered)

        print("Election Title        : " + self.election_info[0])
        print("Voting System         : " + self.election_info[1])
        print("Number of Candidates  : " + str(total_candidates))
        print("Total Registered      : " + str(total_registered))
        print("Total Votes Cast      : " + str(total_votes_cast))
        print("Voters Not Yet Voted  : " + str(voters_not_voted))
        print("Voter Turnout         : " + str(round(turnout_percent, 2)) + "%")

        # Array data structure demonstration: tally audit
        tallies_list = []
        for candidate in self.candidates:
            tallies_list.append(self.votes[candidate])
        audit_array = create_vote_tally_array(tallies_list)
        audit_sum = sum_tally_array(audit_array)
        print("Audit Sum from Array  : " + str(audit_sum) + " votes")

        # Winner or Tie analysis
        result = self.calculate_winner()
        winners = result[0]
        max_votes = result[1]

        if winners is None or total_candidates == 0:
            print("Leader Status         : No candidates available.")
        elif total_votes_cast == 0:
            print("Leader Status         : No votes cast yet (All tied at 0).")
        elif len(winners) == 1:
            print("Current Winner        : " + winners[0] + " with " + str(max_votes) + " votes")
        else:
            print("Current Result        : TIE between " + str(len(winners)) + " candidates")
            print("Tied Candidates       : " + ", ".join(winners))
            print("Highest Vote Count    : " + str(max_votes) + " votes")

        # Status check using bitwise operator
        if has_flag(self.status_flags, FLAG_CLOSED):
            print("Election Status       : Closed")
        elif has_flag(self.status_flags, FLAG_VOTING):
            print("Election Status       : Voting In Progress")
        elif has_flag(self.status_flags, FLAG_SETUP):
            print("Election Status       : Setup Completed")
        else:
            print("Election Status       : Not Started")

        print("========================================")

    def close_election(self):
        """
        Officially closes the election using bitwise flags.
        """
        self.status_flags = set_flag(self.status_flags, FLAG_CLOSED)
