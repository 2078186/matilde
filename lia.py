import math
#define a function nCr(n, r) to calculate the binomial coefficient "n choose r," which represents the number of ways to choose r items from n distinct items without regard to the order. 
#use the math.factorial function to calculate factorials.
def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

def independentAlleles(k,N):
    #This function computes the probability of obtaining a specific number of offspring with a particular genotype in a genetic experiment. It takes two parameters:
    #k: The number of generations.
    #N: The number of offspring having the desired genotype.
    n = 2**k #calculate the total number of offspring in the experiment, which is 2^k (since each generation doubles the number of offspring).
    return sum([nCr(n,m)*(.25**m)*(.75**(n-m)) for m in range(N,n+1)])
#calculate the probability of obtaining exactly N offspring with the desired genotype. I've done this by summing the probabilities of getting exactly m offspring with the desired genotype, where m ranges from N to n.
#for each m, use the binomial coefficient (nCr) to calculate the number of ways to choose m offspring out of n.
#multiply this by the probability of an offspring having the desired genotype (0.25 for a specific genotype) raised to the power m, and the probability of not having the desired genotype (0.75) raised to the power n - m.
print(independentAlleles(6,18))
#print the probability of obtaining N offspring with the desired genotype in the genetic experiment.