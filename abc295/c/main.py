def main():
    # Read input values
    N = int(input())
    A = list(map(int, input().split()))

    # Count the occurrences of each color
    color_count = {}
    for color in A:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # Calculate the total number of pairs
    total_pairs = 0
    for count in color_count.values():
        total_pairs += count // 2

    # Print the total number of pairs
    print(total_pairs)

if __name__ == "__main__":
    main()
