import random

NOTES = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"}

INTERVALS = [("step", 50), ("unison", 25), ("skip", 22.5), ("octave", 2.5)]

SKIP_INTERVALS = [("third", 50), ("sixth", 20), ("fifth", 20), ("fourth", 10)]

DOWN_OR_UP = [("down", 50), ("up", 50)]

NOTE_LENGTHS = [
    ("whole", 2.5),
    ("half", 12.5),
    ("dottedhalf", 10),
    ("quarter", 62.5),
    ("eighth", 12.5),
]

NOTE_COLORS = {
    1: "\033[31m",
    2: "\033[32m",
    3: "\033[33m",
    4: "\033[34m",
    5: "\033[35m",
    6: "\033[36m",
    7: "\033[37m",
}


def select_with_percentage(data):
    total_percentage = sum(percentage for _, percentage in data)
    if total_percentage != 100:
        raise ValueError(
            f"Total percentage should sum up to 100. They currently add up to {total_percentage}."
        )

    random_number = random.randint(1, 100)
    cumulative_percentage = 0
    for item, percentage in data:
        cumulative_percentage += percentage
        if random_number <= cumulative_percentage:
            return item


def interval(note_number):
    interval_type = select_with_percentage(INTERVALS)
    down_or_up = select_with_percentage(DOWN_OR_UP)

    if interval_type == "step":
        note_number += 1 if down_or_up == "up" else -1
    elif interval_type == "unison":
        pass
    elif interval_type == "skip":
        note_number = skip_interval(note_number)
    elif interval_type == "octave":
        note_number += 8 if down_or_up == "up" else -8

    # Limit note number to be less than 7 but no less than 1
    note_number %= 7
    if note_number == 0:
        note_number = 7

    return note_number


def skip_interval(note_number):
    skip_type = select_with_percentage(SKIP_INTERVALS)
    down_or_up = select_with_percentage(DOWN_OR_UP)

    if skip_type == "third":
        note_number += 3 if down_or_up == "up" else -3
    elif skip_type == "sixth":
        note_number += 6 if down_or_up == "up" else -6
    elif skip_type == "fifth":
        note_number += 5 if down_or_up == "up" else -5
    elif skip_type == "fourth":
        note_number += 4 if down_or_up == "up" else -4

    # Limit note number to be less than 7 but no less than 1
    note_number %= 7
    if note_number == 0:
        note_number = 7

    return note_number


def note_length():
    return select_with_percentage(NOTE_LENGTHS)


def generate_notes_list(notes_number: int, add_whole_note_at_end: bool):
    if notes_number < 2:
        exit("The algorithm can only generate with 3 or more notes.")

    if add_whole_note_at_end:
        notes_number -= 1

    notes_number -= 1  # accommodating for the beginning note

    notes_list = [{"number": interval(random.randint(1, 7)), "length": note_length()}]

    for _ in range(notes_number):
        previous_note = notes_list[-1]

        notes_list.append(
            {
                "number": interval(previous_note["number"]),
                "length": note_length(),
            }
        )

    if add_whole_note_at_end:
        new_note_dict = {
            "number": interval(notes_list[-1]["number"]),
            "length": "whole",
        }
        notes_list.append(new_note_dict)

    return notes_list
