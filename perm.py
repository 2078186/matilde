import itertools

def generate_permutations(n):
    # Generate all permutations of length n
    permutations = list(itertools.permutations(range(1, n+1)))

    # Count the total number of permutations
    total_permutations = len(permutations)

    return total_permutations, permutations

def write_output(total, all_permutations):
    # Write the total number of permutations and the list of permutations
    print(total)
    for perm in all_permutations:
        print(" ".join(map(str, perm)))

if __name__ == "__main__":
    # Read the input from a file named "perm2.py"
    with open("perm2.py", "r") as input_file:
        # Input: Positive integer n
        n = int(input_file.readline().strip())

    if n > 7 or n < 1:
        print("Please enter a valid positive integer between 1 and 7.")
    else:
        total, all_permutations = generate_permutations(n)

        # Output the total number of permutations and the list of permutations
        write_output(total, all_permutations)
