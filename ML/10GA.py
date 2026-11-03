#genetic algo
import random

population = ["genetic", "genetec", "genotic", "genttic", "geietic"]

fitness = [7, 6, 5, 4, 5]

def select():
    r = random.uniform(0, sum(fitness))
    total = 0

    for i in range(len(population)):
        total += fitness[i]

        if total >= r:
            return population[i]

parent1 = select()
parent2 = select()

print("Population :", population)
print("Fitness :", fitness)
print("Selected Parent 1 :", parent1)
print("Selected Parent 2 :", parent2)



#Genetic Algorithm to find the word DINOSAURS.

import random

target = "DINOSAURS"
genes = list(set(target))
size = 20

def fitness(word):
    return sum(word[i] == target[i] for i in range(len(target)))

population = [
    [random.choice(genes) for _ in target]
    for _ in range(size)
]

generation = 1

while True:
    population.sort(key=fitness, reverse=True)
    best = population[0]

    print("Generation:", generation, "Best:", "".join(best))

    if fitness(best) == len(target):
        break

    new_population = population[:2]

    while len(new_population) < size:
        p1, p2 = random.choices(population, k=2)
        point = random.randint(1, len(target) - 2)
        child = p1[:point] + p2[point:]

        for i in range(len(child)):
            if random.random() < 0.1:
                child[i] = random.choice(genes)

        new_population.append(child)

    population = new_population
    generation += 1

print("Target Found:", "".join(best))
