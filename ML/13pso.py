import random

food = random.randint(1, 20)
birds = [random.uniform(1, 20) for _ in range(4)]
v = [0] * 4

pbest = birds.copy()

def fitness(x):
    return abs(x - food)

gbest = min(pbest, key=fitness)

for _ in range(100):
    for i in range(4):
        v[i] = (0.5 * v[i]
                + 1.5 * random.random() * (pbest[i] - birds[i])
                + 1.5 * random.random() * (gbest - birds[i]))

        birds[i] += v[i]

        if fitness(birds[i]) < fitness(pbest[i]):
            pbest[i] = birds[i]

    gbest = min(pbest, key=fitness)

    if fitness(gbest) < 0.05:
        break

print("Food Position:", food)
print("Best Bird Position:", round(gbest, 3))
print("Minimum Distance:", round(fitness(gbest), 3))

if fitness(gbest) < 0.05:
    print("Food Found!")
else:
    print("Food Not Found")
