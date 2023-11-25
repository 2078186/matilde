import itertools

def ordered_strings(alphabet, n):
    #The ordered_strings function takes an alphabet (a list of symbols) and a length n.
    #It uses itertools.product to generate all possible combinations of symbols of length n.
    #The result is a list of strings, each representing an ordered string.
    symbols = ''.join(alphabet)
    return [''.join(combination) for combination in itertools.product(symbols, repeat=n)]

if __name__ == "__main__":
    # Read the input
    with open("lexf2.py", "r") as file:
        alphabet = file.readline().split()
        n = int(file.readline())

    # Generate and print the ordered strings
    result = ordered_strings(alphabet, n)
    result.sort()  # Sort the list in-place
    print(*result, sep='\n')
