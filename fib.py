#Looking at the exercise, I can notice that it takes 1 month for the offspring(small rabbits) to become adults(large rabbits).
#the population for each month is determined by the months before it. If we look at the fifth month there are five rabbits, this is because the population grows as a Fibonacci sequence, by adding the number of rabbits in the fourth and third generations together, we can finally get the total number of rabbits in the current generation.
#The function 'Wascally_Wabbits' calculates the number of rabbits after a specified number of months using a recursive approach.
#It takes two parameters: month (the number of months to simulate) and offspringCount (the number of offspring produced by each pair of rabbits).
def Wascally_Wabbits(month,offspringCount):
#during the first month there will be only one pair of rabbits so I defined a condition for that.
    if month==1:
        return 1
#Instead in the case of the second and third month, the number of rabbit’s follows a different pattern.
#By adding the values of the second month and first month together I obtain  the correct value for the third month.
    elif month==2:
     return offspringCount
#In order to keep calling the function until the base cases are reached, I use the Fibonacci's sequence which is'F(n) = F(n-1) + F(n-2)'.
    oneGen=Wascally_Wabbits(month-1,offspringCount)
    twoGen=Wascally_Wabbits(month-2,offspringCount)
#he offspring from the last two months are simply summed because they are not yet mature enough to reproduce.
    if month<=4:
     return(oneGen+twoGen)

    return(oneGen+(twoGen*offspringCount))
#The function continues to call itself recursively until it reaches the specified month.
print(Wascally_Wabbits(36,4))
#The result returned is the number of rabbits after 36 months of reproduction.
 