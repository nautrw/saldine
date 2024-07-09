import random

NOTES = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"}

# step, unison, third, sixth, fifth, fourth, octave
INTERVALS = [1, 0, 3, 6, 5, 4, 8]
INTERVAL_WEIGHTS = [50, 25, 11.25, 4.5, 4.5, 2.25, 2.5]

NOTE_LENGTHS = ["whole", "half", "dottedhalf", "quarter", "eighth"]
NOTE_LENGTH_WEIGHTS = [2.5, 12.5, 10, 62.5, 12.5]


def interval(note_number: int, go_down: bool) -> int:
    interval = random.choices(INTERVALS, weights=INTERVAL_WEIGHTS)[0]

    interval = -interval if go_down else interval
    note_number += interval

    return (note_number % 7) or 7


def note_length() -> str:
    return random.choices(NOTE_LENGTHS, weights=NOTE_LENGTH_WEIGHTS)[0]


def generate_notes_list(
    notes_number: int, add_whole_note_at_end: bool
) -> list[dict[str, int | str]]:
    if notes_number < 3:
        raise ValueError("The algorithm can only generate with 3 or more notes.")

    notes_number -= (
        2 if add_whole_note_at_end else 1
    )  # accommodating for the beginning note and note at end

    notes_list = [
        {
            "number": interval(random.randint(1, 7), random.choice([True, False])),
            "length": note_length(),
        }
    ]

    previous_note = notes_list[-1]

    notes_list.extend(
        {
            "number": interval(
                int(previous_note["number"]), random.choice([True, False])
            ),
            "length": note_length(),
        }
        for _ in range(notes_number)
    )

    if add_whole_note_at_end:
        new_note_dict = {
            "number": interval(
                int(previous_note["number"]), random.choice([True, False])
            ),
            "length": "whole",
        }
        notes_list.append(new_note_dict)

    return notes_list
