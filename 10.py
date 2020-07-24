"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

primes = []

def prime(n):
    is_prime = [True for i in range(0, n+1)]

    p = 2

    while p*p <= n:
        if is_prime[p]:
            i = p*2
            while i<=n:
                is_prime[i] = False
                i+=p
        p+=1
    is_prime[0] = False
    is_prime[1] = False
    for i in range(0, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
target = 10

prime(target)

print(sum(primes))