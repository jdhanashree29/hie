
import random

graph = {
    'A': {'B': 10, 'C': 10, 'D': 30},
    'B': {'A': 10, 'C': 40, 'D': 10},
    'C': {'A': 10, 'B': 40, 'D': 20},
    'D': {'A': 30, 'B': 10, 'C': 20}
}

pheromone = {edge: 1 for edge in
             [('A','B'), ('A','C'), ('A','D'),
              ('B','C'), ('B','D'), ('C','D')]}

for iteration in range(50):
    paths = []

    for ant in range(4):
        path = ['A']
        while len(path) < 4:
            current = path[-1]
            choices = [v for v in graph[current] if v not in path]
            weights = [pheromone[tuple(sorted((current,v)))] /
                       graph[current][v] for v in choices]
            path.append(random.choices(choices, weights=weights)[0])

        path.append('A')
        paths.append(path)

    # Pheromone evaporation
    for edge in pheromone:
        pheromone[edge] *= 0.9

    # Update pheromones
    for path in paths:
        distance = sum(graph[path[i]][path[i+1]]
                       for i in range(4))
        for i in range(4):
            edge = tuple(sorted((path[i], path[i+1])))
            pheromone[edge] += 1 / distance

best = min(paths, key=lambda p: sum(
    graph[p[i]][p[i+1]] for i in range(4)))

print("Best Path:", best)
print("Total Distance:", sum(
    graph[best[i]][best[i+1]] for i in range(4)))
