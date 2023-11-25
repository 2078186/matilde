def compute_failure_array(s):
    #This function calculates the failure array for a given string s.
    #The failure array is used in the KMP algorithm for efficient string matching.
    #It iterates through the characters of the string, updating the failure array based on the previous character matches.
    n = len(s)
    failure_array = [0] * n

    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = failure_array[j - 1]

        if s[i] == s[j]:
            j += 1

        failure_array[i] = j

    return failure_array

if __name__ == "__main__":
    # Read the input DNA string
    with open("kmp1.py", "r") as file:
        file.readline()  # Skip the first line (FASTA header)
        dna_string = file.read().replace("\n", "")

    # Calculate the failure array
    failure_array = compute_failure_array(dna_string)

    # Print the result
    print(" ".join(map(str, failure_array)))
