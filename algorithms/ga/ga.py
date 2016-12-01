import copy
import math
import random
import sys

#problemas
sys.path.append('../../problems/tsp')
import tsp

problem = tsp

problem.read_instance("../../problems/tsp/instances/att48.tsp")

CROMOSSOME_SIZE = problem.NUM_POINTS
POPULATION_SIZE = 10
MAX_EVALUATIONS = 100
SELECTION_SIZE = 2

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
    cut_point = random.randint(0, CROMOSSOME_SIZE-1)
    offspring = []
    for i in range(CROMOSSOME_SIZE):

        if i > cut_point:
            offspring = parents[1][i]
            offspring[1][i] = parents[0][i]
        else:

    return offspring


def apply_mutation(offspring):
    pass


def replacement(population, offspring):
    pass


def update_progress():
    global evaluations
    evaluations += POPULATION_SIZE


def executar():
    population = create_population(5)
    evaluate_population(population)
    #while(evaluations < MAX_EVALUATIONS):
    parents = select_parents(population)
        #offspring = apply_crossover(parents)
        #offspring = apply_mutation(offspring)
        #evaluate_population(offspring)
        #population = replacement(population, offspring)
        #update_progress()
    return population

population = executar()
for cromossome in population:
    print(cromossome.fitness)
