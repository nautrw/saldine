import random
import signal
import sys

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

NOTE_LENGTH_LETTERS = {
    "whole": "WH",
    "dottedhalf": "DH",
    "half": "HA",
    "quarter": "QU",
    "eighth": "EI",
}

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
        )  # Make it more intuitive if these problems happen again

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
    note_length_type = select_with_percentage(NOTE_LENGTHS)

    return NOTE_LENGTH_LETTERS[note_length_type]


def parse_notes(notes_list):
    formatted_notes_list = []

    for note_dict in notes_list:
        note_name = NOTES[note_dict["number"]]
        color = NOTE_COLORS[note_dict["number"]]
        formatted_notes_list.append(f'{color}{note_name}{note_dict["length"]}\033[m')

    return " ".join(formatted_notes_list)


def ask_run_again():
    if input(
        "Run the program again? \033[90m[Y/n] \033[32m->\033[m "
    ).strip().lower() not in ("y", ""):
        print("Stopping program.")
        sys.exit()


def main():
    while True:
        try:
            notes_number = int(input("How many notes do you want? \033[32m->\033[m "))
        except ValueError:
            print("The number of notes must be an integer (no decimals!)")
            ask_run_again()
            continue

        if notes_number < 2:
            print("The number of notes must be more than 2")
            ask_run_again()
            continue

        add_whole_note_at_end = input(
            "Add whole note at end? \033[90m[Y/n] \033[32m->\033[m "
        ).strip().lower() in ("y", "")

        notes_number -= 1  # Acommodating for the note at the beginning

        if add_whole_note_at_end:  # Acommodating for the end note if chosen
            notes_number -= 1

        notes_list = [{"number": random.randint(1, 7), "length": note_length()}]

        for _ in range(notes_number):
            previous_note = notes_list[-1]
            new_note_dict = {
                "number": skip_interval(previous_note["number"]),
                "length": note_length(),
            }

            notes_list.append(new_note_dict)

        if add_whole_note_at_end:
            new_note_dict = {
                "number": skip_interval(notes_list[-1]["number"]),
                "length": NOTE_LENGTH_LETTERS["whole"],
            }

            notes_list.append(new_note_dict)

        print(parse_notes(notes_list), "\n")
        ask_run_again()


def hard_exit(sig, frame):
    print("\nStopping program.")
    sys.exit()


signal.signal(signal.SIGINT, hard_exit)
