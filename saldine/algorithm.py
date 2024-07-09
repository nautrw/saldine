import random
from dataclasses import dataclass

NOTES = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"}

# step, unison, third, sixth, fifth, fourth, octave
INTERVALS = [1, 0, 3, 6, 5, 4, 8]
INTERVAL_WEIGHTS = [50, 25, 11.25, 4.5, 4.5, 2.25, 2.5]

NOTE_LENGTHS = ["whole", "half", "dottedhalf", "quarter", "eighth"]
NOTE_LENGTH_WEIGHTS = [2.5, 12.5, 10, 62.5, 12.5]


@dataclass
class Note:
    """The class of a note"""

    number: int
    length: str


def interval(note_number: int, go_down: bool) -> int:
    interval = random.choices(INTERVALS, weights=INTERVAL_WEIGHTS)[0]

    interval = -interval if go_down else interval
    note_number += interval

    return (note_number % 7) or 7


def note_length() -> str:
    return random.choices(NOTE_LENGTHS, weights=NOTE_LENGTH_WEIGHTS)[0]


def generate_notes_list(notes_number: int, add_whole_note_at_end: bool) -> list[Note]:
    if notes_number < 3:
        raise ValueError("The algorithm can only generate with 3 or more notes.")

    notes_list = [Note(number=random.randint(1, 7), length=note_length())]

    previous_note = notes_list[-1]

    for _ in range(notes_number - 1):
        notes_list.append(
            Note(
                number=interval(previous_note.number, random.choice([True, False])),
                length=note_length(),
            )
        )
        previous_note = notes_list[-1]

    if add_whole_note_at_end:
        notes_list[-1].length = "whole"

    return notes_list
