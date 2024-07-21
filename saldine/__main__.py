import signal
import sys

from saldine.algorithm import Note, generate_notes_list

NOTES = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G"}


def hard_exit(signal, frame) -> None:
    """
    Handles a hard exit of the program when a signal is received.

    Args:
        sig: The signal number.
        frame: The current stack frame.

    Returns:
        None
    """

    print("\nStopping program.")
    sys.exit()


signal.signal(signal.SIGINT, hard_exit)


def ask_run_again() -> None:
    """
    Asks the user if they want to run the program again and exits if the input is not 'Y' or empty.

    Returns:
        None
    """

    if input("Run the program again? [Y/n]: ").strip().lower() not in ("y", ""):
        print("Stopping program.")
        sys.exit()


def parse_notes(notes: list[Note]) -> str:
    return " ".join(f"{NOTES[note.number]}:{note.length}" for note in notes)


def main() -> None:
    """
    The main program loop to generate musical notes based on user input.

    Returns:
        None
    """

    while True:
        try:
            notes_number = int(input("How many notes do you want to generate? "))
        except ValueError:
            print("The number of notes must be an integer.")
            ask_run_again()
            continue

        add_whole_note_at_end = input(
            "Do you want to add a whole note at the end? [Y/n]: "
        ).strip().lower() in ("y", "")

        notes_list = generate_notes_list(notes_number, add_whole_note_at_end)

        print(parse_notes(notes_list))
        ask_run_again()


if __name__ == "__main__":
    main()
