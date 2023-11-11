with open ('input7.py', 'r') as file:

 for line in file:
    n=int(line) #Within each iteration, this step allows to convert the content of the line to an integer using int() and assigns the result to the variable n.
#It's important to note that this assignment happens in every iteration of the loop. So, if there are multiple lines in the file, n will be updated with the value of the last line.
print(n-2)
#After the loop completes, the code calculates n - 2 and prints the result. This is done once, and it will be based on the last value of n read from the file.