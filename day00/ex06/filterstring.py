import sys
from ft_filter import ft_filter


def main():
    """
    Filters words in a string longer than a given
    length from command-line arguments.
    Expects two arguments: a string and an integer.
    Prints a list of words longer than the given length.
    """
    args = sys.argv[1:]

    if len(args) != 2:
        print("AssertionError: the arguments are bad")
        return

    input_string = args[0]
    try:
        length = int(args[1])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = input_string.split()

    result = ft_filter(lambda word: len(word) > length, words)

    print(list(result))


if __name__ == "__main__":
    main()
