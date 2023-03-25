def is_happy(substring):
    # Count the occurrences of each digit
    digit_count = {}
    for digit in substring:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    # Check if the counts are even, which means the substring can be rearranged into a happy string
    for count in digit_count.values():
        if count % 2 != 0:
            return False
    return True


def main():
    # Read the input string
    S = input()

    # Initialize the counter for happy substrings
    happy_count = 0

    # Iterate through all possible contiguous substrings of S
    for l in range(len(S)):
        for r in range(l + 1, len(S) + 1, 2):  # Increment by 2 to check only even-length substrings
            if is_happy(S[l:r]):
                happy_count += 1

    # Print the final counter value
    print(happy_count)

if __name__ == "__main__":
    main()
