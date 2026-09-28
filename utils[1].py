"""
utils.py - Helper utilities for Election Simulation.
Provides input validation without exception handling, array tally functions,
bitwise stage flag operations, and percentage calculations.
"""

from array import array

# Bitwise flags for election lifecycle stages
FLAG_SETUP = 1       # binary 001: Election setup completed
FLAG_VOTING = 2      # binary 010: Voting phase active
FLAG_CLOSED = 4      # binary 100: Election officially closed


def has_flag(status_flags, flag):
    """
    Checks if a specific stage flag is set using the bitwise AND operator.
    """
    return (status_flags & flag) == flag


def set_flag(status_flags, flag):
    """
    Sets a specific stage flag using the bitwise OR operator.
    """
    return status_flags | flag


def calculate_percentage(part, whole):
    """
    Calculates percentage using arithmetic operators and operator precedence.
    Guards against division by zero.
    """
    if whole == 0:
        return 0.0
    # Natural operator precedence: division evaluated, then multiplication
    percentage = (part / whole) * 100
    return percentage


def create_vote_tally_array(counts_list):
    """
    Creates a numerical array of signed integers ('i') to store vote tallies.
    Demonstrates Python's standard array data structure.
    """
    return array('i', counts_list)


def sum_tally_array(tally_array):
    """
    Calculates the sum of votes in a numerical array using a simple loop.
    Used for ballot auditing.
    """
    total = 0
    for count in tally_array:
        total += count
    return total


def is_valid_positive_integer(text):
    """
    Validates if input string represents a positive whole number.
    Does NOT use exception handling; uses string methods and relational checks.
    """
    stripped_text = text.strip()
    if not stripped_text.isdigit():
        return False
    number = int(stripped_text)
    if number <= 0:
        return False
    return True
