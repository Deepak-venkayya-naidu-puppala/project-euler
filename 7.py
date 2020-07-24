"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

primes = []

def prime(n):
    is_prime = [True for i in range(0, n)]

    p = 2

    while p*p < n:
        if is_prime[p]:
            i = p*2
            while i<n:
                is_prime[i] = False
                i+=p
        p+=1
    for i in range(0, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
target = 10001

n = 10
while True:
    if len(primes) < target+2:
        primes = []
        prime(n)
        n*=10
    if len(primes)>target:
        break

print(primes[10001+1])
            