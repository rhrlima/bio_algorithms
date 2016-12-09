import math
import random
import sys

POPULATION_SIZE = 100
MAX_EVALUATIONS = 100000
SELECTION_SIZE = 2
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.05

class Cromossome:
    def __init__(self, genes, fitness):
        self.genes = genes;
        self.fitness = fitness


    def copy(self):
        return Cromossome(self.genes[:], self.fitness)


def set_problem(p):
    global problem, CROMOSSOME_SIZE
    problem = p
    CROMOSSOME_SIZE = problem.NUM_POINTS


def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        population.append(Cromossome(problem.create_solution(), -1))
    return population


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
    offspring = parents[0].copy()
    if random.uniform(0, 1) < CROSSOVER_RATE:
        while(True):
            r1 = random.randint(0, CROMOSSOME_SIZE-1)
            r2 = random.randint(0, CROMOSSOME_SIZE-1)
            if r1 < r2: break
        cont = 0
        aux = parents[0].genes[r1:r2]
        for i in range(CROMOSSOME_SIZE):
            if i < r1 or i >= r2:
                for gene in parents[1].genes:
                    if not gene in aux:
                        offspring.genes[i] = gene
                        aux.append(gene)
                        break
            else:
                offspring.genes[i] = aux[cont]
                cont +=1
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


def replacement(population, offspring):
    worst = population[0]
    for cromossome in population:
        if cromossome.fitness > worst.fitness:
            worst = cromossome
    population.remove(worst)
    population.append(offspring.copy())
    return population


def init_progress():
    global evaluations
    evaluations = POPULATION_SIZE


def update_progress():
    global evaluations
    evaluations += POPULATION_SIZE


def execute():
    population = create_population()
    evaluate_population(population)
    init_progress()
    while(evaluations < MAX_EVALUATIONS):
        parents = select_parents(population)
        offspring = apply_crossover(parents)
        apply_mutation(offspring)
        evaluate_solution(offspring)
        population = replacement(population, offspring)
        update_progress()
    return population
