
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def gcd(x, y):
    if  x%y != 0:
        return gcd(y, x%y)
    else:
        return y

lcm  = lambda x, y: x*y // gcd(x, y)

result = 1

for i in range(1, 21):
    result = lcm(result, i)

print(result)