#This function, named hamm, is defined to calculate the Hamming distance between two input strings, string1 and string2.
def hamm(string1, string2):
    #Initializes a variable called distance to 0, which will be used to keep track of the Hamming distance.
    distance = 0
    #Include an assert statement to check whether the lengths of string1 and string2 are equal. 
    #This is essential because Hamming distance is only defined for strings of equal length.
    #If the lengths are not equal, an AssertionError is raised to indicate that there is an issue with the input data.
    assert len(string1) == len(string2)
    #Enter a loop that iterates through the indices of the strings, from 0 to len(string1) - 1.
    for i in range(len(string1)):
        #Inside the loop, compare the characters at the same position in string1 and string2.
        #If they are different, it increments the distance variable by 1. This is how I calculated the Hamming distance.
        if string1[i] != string2[i]:
            distance += 1
    return distance
# to ensure the code doesn't run when the script is imported as a module into another script, I use:
if __name__ == "__main__":
    #then the code will open the file given by rosalind.
    with open("hamm.pyy.py", "r") as file:
        string1 = file.readline().strip()
        string2 = file.readline().strip()
    print(hamm(string1, string2))