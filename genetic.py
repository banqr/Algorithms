import random
import math

#pravi jednu jedinu populaciju tj hromozom
def kreiraj_populaciju(duzina, geneset):
    population = random.sample(geneset, duzina)
    return ''.join(population)


#fitness funkcija sa list comp-om
def fitness(hromozom, target):
    genotype = [1 if w == y else 0 for w, y in zip(hromozom, target)]
    score = math.ceil(sum(genotype)/len(target)*100)
    return score


#crossover funkcija
def crossover(matingpool):
    parentA_random_int = random.randint(0, len(matingpool)-1)
    parentB_random_int = random.randint(0, len(matingpool)-1)
    
    parentA = matingpool[parentA_random_int]
    parentB = matingpool[parentB_random_int]
    
    midpoint = random.randint(0, len(target)-1)
    
    pismo_glava = random.random()
    
    if pismo_glava <= 0.5:
        child = parentA[midpoint:] + parentB[:midpoint]
    else:
        child = parentA[:midpoint] + parentB[midpoint:]
    return child

#mutate funkcija
def mutation(mutation_rate, child):
    random_letter = random.choice(geneset)
    random_gene = random.randint(0, len(target)-1)
    child_list = []
    child_list = list(child)
    
    if random.random() < mutation_rate:
        child_list[random_gene] = random_letter
    return ''.join(child_list)

def evolve(populacija, target):
    mating_pool = []
    parents = []
    
    for pop in populacija:
        fitness(pop, target)    
        if fitness(pop, target) > 0:
            mating_pool.extend([pop] * fitness(pop, target))   
    
    for i in range(broj_populacije):
        child = crossover(mating_pool)
        child = mutation(mutation_rate, child)
        parents.append(child)
    
    return parents


geneset = " abcdefghijklmnopqrstuvwxyz"
target = "to be or not to be"
broj_populacije = 500
mutation_rate = 0.01
populacija = [kreiraj_populaciju(len(target), geneset) for x in range(broj_populacije)]
brojac_generacija = 0
print(populacija[:50])
print('###########################################')
for i in range(500):
    brojac_generacija += 1
    populacija = evolve(populacija, target)
    if target in populacija:
        break
print("Uspeh nakon " + str(brojac_generacija) + ' generacija')
print(populacija)