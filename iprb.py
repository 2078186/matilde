 # Function definition takes three input values: k, m, and n.
def iprb(k, m, n):
#k represents the number of individuals that are homozygous dominant for a particular trait.
#m represents the number of individuals that are heterozygous for the trait.
#n represents the number of individuals that are homozygous recessive for the trait.
# I calculate the probability of selecting an individual with a dominant allele (heterozygous or homozygous dominant) from a random population.
#The formula uses combinatorial principles, where i represents the total number of possible combinations of two alleles selected from the population, and j represents the total number of possible combinations of two alleles from the entire population.
#The formula effectively calculates the probability of selecting a dominant allele and subtracts it from 1 to obtain the probability of selecting a non-dominant allele (recessive).
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m
    j = 4 * (k + m + n) * (k + m + n - 1)
    rst = 1 - float(i) / j
    return rst
#read input values for k, m, and n from the first line of a file named "iprb.py."
#assume that the values are integers separated by spaces.
#these values are used as inputs to the iprb function.
if __name__ == "__main__":
    with open("iprb.py", 'r') as file:
        k, m, n = map(int, file.readline().strip().split(" "))
        #then the code prints the calculated probability.
        print(iprb(k, m, n))