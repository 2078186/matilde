def calculate_double_factorial_modulo(n, modulo):
    #This function calculates the double factorial of a given number n modulo a specified value.
    #The result is updated by multiplying the current value of result with the current value of i, and then taking the modulo of the result.
    result = 1
    for i in range(n, 0, -2):
        result = (result * i) % modulo
    return result

def calculate_b_n_modulo_m(n, modulo=1000000):
    if n == 1:
        return 1
    else:
        return calculate_double_factorial_modulo(2 * n - 5, modulo)

# Sample dataset:
n = int(987)
result = calculate_b_n_modulo_m(n)
print(result)
#I set the value of n to 5.
#then calculate b_n modulo 1000000 using the calculate_b_n_modulo_m function.
#Finally, the code prints the result.