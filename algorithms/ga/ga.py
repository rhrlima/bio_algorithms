import copy
import math
import random
import sys

#problemas
sys.path.append('../../problems/tsp')
import tsp

problem = tsp

problem.read_instance("../../problems/tsp/instances/test4.tsp")

CROMOSSOME_SIZE = problem.NUM_POINTS
POPULATION_SIZE = 100
MAX_EVALUATIONS = 10000
SELECTION_SIZE = 2
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.1

evaluations = 0

class Cromossome:
    def __init__(self, genes):
        self.genes = genes;
        self.fitness = -1


def create_population(population_size):
    aux = []
    for i in range(population_size):
        aux.append(Cromossome(problem.create_solution()))
    return aux


def evaluate_population(population):
    for cromossome in population:
        evaluate_solution(cromossome)


def evaluate_solution(cromossome):
    cromossome.fitness = problem.evaluate_solution(cromossome.genes)


def select_parents(population):
    parents = []
    for i in range(2):
        tournament = []
        while(len(tournament) < SELECTION_SIZE):
            solution = population[random.randint(0, len(population)-1)]
            if not solution in tournament:
                tournament.append(solution)
        best = tournament[0]
        for solution in tournament:
            if solution.fitness < best.fitness:
                best = solution
        parents.append(best)
    return parents


def apply_crossover(parents):
    offspring = copy.deepcopy(parents[0])
    if random.uniform(0, 1) < CROSSOVER_RATE:
        cut_point = random.randint(0, CROMOSSOME_SIZE-1)
        for i in range(CROMOSSOME_SIZE):
            if i > cut_point:
                offspring.genes[i] = copy.deepcopy(parents[1].genes[i])
    return offspring


def apply_mutation(offspring):
    if random.uniform(0, 1) < MUTATION_RATE:
        while(True):
            r1 = random.randint(0, CROMOSSOME_SIZE-1)
            r2 = random.randint(0, CROMOSSOME_SIZE-1)
            if r1 != r2: break
        aux = offspring.genes[r1]
        offspring.genes[r1] = offspring.genes[r2]
        offspring.genes[r2] = aux
    return offspring


def replacement(population, offspring):
    worst = population[0]
    for cromossome in population:
        if cromossome.fitness > worst.fitness:
            worst = cromossome
    population.remove(worst)
    population.append(copy.deepcopy(offspring))
    return population


def update_progress():
    global evaluations
    evaluations += POPULATION_SIZE


def print_solution(cromossome):
    for gene in cromossome.genes:
        print(gene.id, end=" ")
    print("\t", cromossome.fitness, "")


def executar():
    population = create_population(POPULATION_SIZE)
    evaluate_population(population)
    while(evaluations < MAX_EVALUATIONS):
        parents = select_parents(population)
        offspring = apply_crossover(parents)
        offspring = apply_mutation(offspring)
        evaluate_solution(offspring)
        population = replacement(population, offspring)
        population.sort(key = lambda c: c.fitness)
        print("best: ", end="")
        print_solution(population[0])
        update_progress()
    return population

population = executar()
population.sort(key = lambda c: c.fitness)
print("Final best: ", end="")
print_solution(population[0])
