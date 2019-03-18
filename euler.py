#Problem 1

maks = 1000

def multiples(max):
    sum = 0

    for i in range(1, max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    return sum

print(multiples(maks))