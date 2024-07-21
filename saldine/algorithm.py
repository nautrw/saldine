import random
from dataclasses import dataclass

# step, unison, third, sixth, fifth, fourth, octave
INTERVALS = [1, 0, 3, 6, 5, 4, 8]
INTERVAL_WEIGHTS = [50, 25, 11.25, 4.5, 4.5, 2.25, 2.5]

NOTE_LENGTHS = [1, 2, 3, 4, 8]
NOTE_LENGTH_WEIGHTS = [2.5, 12.5, 10, 62.5, 12.5]


@dataclass
class Note:
    """
    A data class representing a musical note with a number and length.

    Args:
        number (int): The numerical value of the note.
        length (str): The length of the note.

    Returns:
        None
    """

    number: int
    length: int


def interval(note_number: int, go_down: bool) -> int:
    """
    Calculates the new note number based on the given note number and direction.

    Args:
        note_number (int): The current note number.
        go_down (bool): A flag indicating whether to go down or up.

    Returns:
        int: The new note number after applying the interval calculation.
    """

    interval = random.choices(INTERVALS, weights=INTERVAL_WEIGHTS)[0]

    interval = -interval if go_down else interval
    note_number += interval

    return (note_number % 7) or 7


def note_length() -> int:
    """
    Returns a randomly selected note length based on predefined weights.

    Returns:
        str: A randomly selected note length.
    """

    return random.choices(NOTE_LENGTHS, weights=NOTE_LENGTH_WEIGHTS)[0]


def generate_notes_list(notes_number: int, add_whole_note_at_end: bool) -> list[Note]:
    """
    Generates a list of musical notes based on the specified number of notes and an option to add a whole note at the end.

    Args:
        notes_number (int): The number of notes to generate (must be 3 or more).
        add_whole_note_at_end (bool): A flag indicating whether to add a whole note at the end.

    Returns:
        list[Note]: A list of generated musical notes.
    Raises:
        ValueError: If notes_number is less than 3.
    """

    if notes_number < 3:
        raise ValueError("The algorithm can only generate with 3 or more notes.")

    notes_list = [Note(number=random.randint(1, 7), length=note_length())]

    notes_list.extend(
        Note(
            number=interval(notes_list[-1].number, random.choice([True, False])),
            length=note_length(),
        )
        for _ in range(notes_number - 1)
    )

    if add_whole_note_at_end:
        notes_list[-1].length = 1

    return notes_list
