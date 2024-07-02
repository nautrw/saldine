import random

NOTES = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"}

# step, unison, third, sixth, fifth, fourth, octave
INTERVALS = [1, 0, 3, 6, 5, 4, 8]
INTERVAL_WEIGHTS = [50, 25, 11.25, 4.5, 4.5, 2.25, 2.5]

NOTE_LENGTHS = ["whole", "half", "dottedhalf", "quarter", "eighth"]
NOTE_LENGTH_WEIGHTS = [2.5, 12.5, 10, 62.5, 12.5]

NOTE_COLORS = {
    1: "\033[31m",
    2: "\033[32m",
    3: "\033[33m",
    4: "\033[34m",
    5: "\033[35m",
    6: "\033[36m",
    7: "\033[37m",
}


def interval(note_number: int, go_down: bool):
    interval = random.choice(INTERVALS, weights=INTERVAL_WEIGHTS)

    interval = -interval if go_down else interval
    note_number += interval

    return (note_number % 7) or 7


def note_length():
    return random.choice(NOTE_LENGTHS, weights=NOTE_LENGTH_WEIGHTS)


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
