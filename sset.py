def count_subsets_modulo(n):
    #The count_subsets_modulo function takes an integer n as input.
    #It calculates 2 to the power of n (2 ** n) and then takes the result modulo 1,000,000.
    #The function returns this result.
    return (2 ** n) % 1_000_000

if __name__ == "__main__":
    # Read the input
    with open("sset1.py", "r") as file:
        n = int(file.readline())

    # Calculate and print the result
    result = count_subsets_modulo(n)
    print(result)
