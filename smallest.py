## Basic "find amallest" algo.
brojevi = [54, 13, 5, 9, 108, 4]

def find_smallest(niz):
    smallest = niz[0]

    for i, j in enumerate(niz):
        if niz[i] < smallest:
            smallest = niz[i]
    
    return smallest

print(find_smallest(brojevi))