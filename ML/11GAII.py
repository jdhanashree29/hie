#Implement Tournament selection ,Rank selection  for India problem.

import random

population = [
    ["Bangalore", "Pune", "Hyderabad", "Jaipur"],
    ["Pune", "Bangalore", "Jaipur", "Hyderabad"],
    ["Hyderabad", "Jaipur", "Pune", "Bangalore"],
    ["Jaipur", "Hyderabad", "Bangalore", "Pune"],
    ["Bangalore", "Hyderabad", "Pune", "Jaipur"]
]

fitness = [72, 90, 65, 88, 78]

print("Population and Fitness:")
for p, f in zip(population, fitness):
    print(p, "Fitness =", f)

# ---------------- Tournament Selection ----------------

print("\nTournament Selection")

selected = random.sample(range(5), 3)

for i in selected:
    print(population[i], "Fitness =", fitness[i])

winner = max(selected, key=lambda i: fitness[i])

print("\nTournament Winner:")
print(population[winner], "Fitness =", fitness[winner])

# ---------------- Rank Selection ----------------
print("\nRank Selection")

ranked = sorted(range(5), key=lambda i: fitness[i])

for rank, i in enumerate(ranked, 1):
    print("Rank =", rank, population[i], "Fitness =", fitness[i])

winner = random.choices(ranked, weights=range(1,6), k=1)[0]

print("\nRank Selection Winner:")
print(population[winner], "Fitness =", fitness[winner])








#Compare all selections and find the suitable one.

import random

population = [
    ["Bangalore","Pune","Hyderabad","Jaipur"],
    ["Pune","Bangalore","Jaipur","Hyderabad"],
    ["Hyderabad","Jaipur","Pune","Bangalore"],
    ["Jaipur","Hyderabad","Bangalore","Pune"],
    ["Bangalore","Hyderabad","Pune","Jaipur"]
]

fitness = [72, 90, 65, 88, 78]

print("Population and Fitness:")
for p, f in zip(population, fitness):
    print(p, "Fitness =", f)

t = random.sample(range(5), 3)
winner1 = max(t, key=lambda i: fitness[i])

print("\nTournament Winner:")
print(population[winner1], "Fitness =", fitness[winner1])
n
ranked = sorted(range(5), key=lambda i: fitness[i])
winner2 = random.choices(ranked, weights=range(1,6), k=1)[0]

print("\nRank Selection Winner:")
print(population[winner2], "Fitness =", fitness[winner2])

winner3 = random.choices(range(5), weights=fitness, k=1)[0]

print("\nRoulette Wheel Winner:")
print(population[winner3], "Fitness =", fitness[winner3])

best = fitness.index(max(fitness))

print("\nOverall Best:")
print(population[best], "Fitness =", fitness[best])




#Apply genetic algorithms for Assigning Jobs to machine.

import random
import matplotlib.pyplot as plt

jobs = ["J1","J2","J3","J4"]
times = [4,6,3,5]
machines = ["M1","M2","M3"]

size = 20
mutation_rate = 0.1
generations = 100

def create_population():
    return [[random.choice(machines) for _ in jobs]
            for _ in range(size)]

def makespan(ch):
    load = [0, 0, 0]

    for i in range(4):
        m = machines.index(ch[i])
        load[m] += times[i]

    return max(load)

def fitness(ch):
    return 100 / makespan(ch)

def roulette(pop):
    return random.choices(
        pop,
        weights=[fitness(x) for x in pop],
        k=1
    )[0]

def tournament(pop):
    group = random.sample(pop, 3)
    return min(group, key=makespan)

def rank(pop):
    ranked = sorted(pop, key=makespan)

    weights = list(range(len(ranked), 0, -1))

    return random.choices(
        ranked,
        weights=weights,
        k=1
    )[0]

def crossover(p1, p2):
    point = random.randint(1, 3)
    return p1[:point] + p2[point:]

def mutate(child):
    for i in range(4):
        if random.random() < mutation_rate:
            child[i] = random.choice(machines)
    return child

def run(select):
    pop = create_population()

    for generation in range(generations):

        new_pop = []

        for i in range(size):
            p1 = select(pop)
            p2 = select(pop)

            child = crossover(p1, p2)
            child = mutate(child)

            new_pop.append(child)

        pop = new_pop

    best = min(pop, key=makespan)

    return best, makespan(best)


methods = {
    "Roulette": roulette,
    "Tournament": tournament,
    "Rank": rank
}

results = {}

for name, method in methods.items():

    best, score = run(method)

    results[name] = score

    print("\n", name)
    print("Assignment:", dict(zip(jobs, best)))
    print("Makespan:", score)

best_method = min(results, key=results.get)

print("\nBest Method:", best_method)
print("Best Makespan:", results[best_method])

plt.bar(results.keys(), results.values())
plt.xlabel("Selection Method")
plt.ylabel("Makespan")
plt.title("Selection Method Comparison")
plt.show()    




###B. Travelling Sales man


import random
import matplotlib.pyplot as plt

cities = ["A", "B", "C", "D", "E"]

dist = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 17],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 12],
    [25, 17, 20, 12, 0]
]

def cost(route):
    return sum(dist[route[i]][route[(i+1) % 5]] for i in range(5))

def fitness(route):
    return 1 / cost(route)

def select(pop):
    return random.choices(pop, weights=[fitness(x) for x in pop])[0]

def crossover(p1, p2):
    a, b = sorted(random.sample(range(5), 2))
    child = p1[a:b] + [c for c in p2 if c not in p1[a:b]]
    return child

def mutate(route):
    if random.random() < 0.2:
        a, b = random.sample(range(5), 2)
        route[a], route[b] = route[b], route[a]
    return route

pop = [random.sample(range(5), 5) for _ in range(20)]

for _ in range(200):
    new = [min(pop, key=cost)]
    while len(new) < 20:
        child = crossover(select(pop), select(pop))
        new.append(mutate(child))
    pop = new

best = min(pop, key=cost)

print("Best Route:", [cities[i] for i in best] + [cities[best[0]]])
print("Minimum Distance:", cost(best))

x = [best[0]] + best + [best[0]]
plt.plot(x, marker="o")
plt.title("TSP Best Route")
plt.xlabel("Route Position")
plt.ylabel("City Index")
plt.show()




###C. Knapsack


import random

weights = [2, 3, 4, 5, 6]
values = [3, 4, 5, 6, 10]
capacity = 10

def fitness(ch):
    w = sum(ch[i] * weights[i] for i in range(5))
    v = sum(ch[i] * values[i] for i in range(5))
    return v if w <= capacity else 0

def select(pop):
    return random.choices(pop, weights=[fitness(x) + 1 for x in pop])[0]

def crossover(p1, p2):
    point = random.randint(1, 4)
    return p1[:point] + p2[point:]

def mutate(ch):
    i = random.randint(0, 4)
    ch[i] = 1 - ch[i]
    return ch

pop = [[random.randint(0, 1) for _ in range(5)] for _ in range(20)]

for _ in range(100):
    new = [max(pop, key=fitness)]
    while len(new) < 20:
        child = crossover(select(pop), select(pop))
        new.append(mutate(child))
    pop = new

best = max(pop, key=fitness)

print("Selected Items:", best)
print("Total Weight:", sum(best[i] * weights[i] for i in range(5)))
print("Total Value:", fitness(best))





###D. Finding best candidate for job


import random

candidates = ["A", "B", "C", "D", "E"]
skills = [8, 6, 9, 7, 5]
experience = [7, 9, 6, 8, 4]
communication = [8, 7, 9, 6, 8]

def fitness(ch):
    i = ch[0]
    return skills[i] + experience[i] + communication[i]

def select(pop):
    return max(random.choices(pop, k=3), key=fitness)

def crossover(p1, p2):
    return random.choice([p1, p2]).copy()

def mutate(ch):
    if random.random() < 0.2:
        ch[0] = random.randint(0, 4)
    return ch

pop = [[random.randint(0, 4)] for _ in range(10)]

for _ in range(50):
    new = [max(pop, key=fitness)]
    while len(new) < 10:
        child = crossover(select(pop), select(pop))
        new.append(mutate(child))
    pop = new

best = max(pop, key=fitness)
i = best[0]

print("Best Candidate:", candidates[i])
print("Fitness Score:", fitness(best))
