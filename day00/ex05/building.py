import sys
import string


def count_text(text: str) -> tuple[int, int, int, int, int]:
    """
    Counts different character types in a given text.
    Returns a tuple of:
    (uppercase letters, lowercase letters, punctuation marks, spaces, digits)
    """
    upper = sum([1 for c in text if c.isupper()])
    lower = sum([1 for c in text if c.islower()])
    punct = sum([1 for c in text if c in string.punctuation])
    spaces = text.count(" ")
    digits = sum([1 for c in text if c.isdigit()])
    return upper, lower, punct, spaces, digits


def main():
    """
    Entry point of the program.
    Accepts one optional command-line argument (text),
    or reads input from the user if no argument is given.
    Counts and prints the number of uppercase,
    lowercase, punctuation, spaces, and digits.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        try:
            raw = sys.stdin.readline()
            if raw.endswith("\n"):
                text = raw.rstrip("\n") + " "
            else:
                text = raw
        except EOFError:
            text = ""

    upper, lower, punct, spaces, digits = count_text(text)

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
