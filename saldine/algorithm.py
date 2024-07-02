import random

NOTES = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"}

# step, unison, third, sixth, fifth, fourth, octave
INTERVALS = [(1, 50), (0, 25), (3, 11.25), (6, 4.5), (5, 4.5), (4, 2.25)(8, 2.5)]

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


def interval(note_number: int, go_down: bool):
    interval = select_with_percentage(INTERVALS)

    interval = -interval if go_down else interval
    note_number += interval

    return (note_number % 7) or 7


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
