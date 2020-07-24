# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


question = 13195 

div = 2
while question != 0:
    if question%div != 0:
        div = div+1
    else:
        maxFact = question
        question = question/div
        if question == 1:
            result = maxFact
            break

print(int(result))