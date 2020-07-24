# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


result = 0

i = 1

while 3*i<=1000 or 5*i<=1000:
    if 3*i<=1000:
        result += (3*i)
    if 5*i<=1000:
        result += (5*i)
    i+=1

print(result)
