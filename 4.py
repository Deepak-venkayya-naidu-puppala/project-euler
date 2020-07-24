"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
largest = 0

for first in range(999, 100, -1):
    for second in range(first, 100, -1):
        x = first*second
        if x > largest:
            s = str(x)
            if s == s[::-1]:
                largest = x
print(largest)