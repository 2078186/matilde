#The num_rabbits(n, m) function takes two parameters:
#n: The number of months for which you want to calculate the number of rabbits.
#m: The number of months a rabbit lives before it dies.
def num_rabbits(n, m):
  #initialize a list num_list to store the number of rabbits for each month.
  #start with two initial values: 0 and 1 (assuming there are no rabbits in month 0 and one rabbit in month 1).
    num_list = []
    num_list.append(0)
    num_list.append(1)
    #use a loop to calculate the number of rabbits for each month from the 2nd month (i = 2) up to the given month n.
    # #The calculations resemble a modified Fibonacci sequence.
#If i is less than m, the code adds the number of rabbits in the previous month and the month before the first death (num_list[i] + num_list[i-1]).
#If i is equal to m, the code adds the number of rabbits in the previous month and the month before the first death, subtracting the number of rabbits that die in the current month (num_list[i] + num_list[i-1] - num_list[i-m+1]).
#If i is greater than m, the code is the same of 'if i is equal to m'.
    for i in range(1, n+1, 1):
        if i < m:
            num_list.append(num_list[i] + num_list[i-1])
        if i == m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
        if i > m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])
    
    # print(num_list)
    return num_list[n]

if __name__ == "__main__":
    with open("fibd11.py", "r") as file:
        n, m = map(int, file.readline().strip().split(" "))
    print(num_rabbits(n, m))
    #calculate the number of rabbits alive in each month up to the given month n, taking into account the lifespan of a rabbit, which is m months.
    #the code resembles the Fibonacci sequence but with the modification of rabbit deaths after a certain number of months.