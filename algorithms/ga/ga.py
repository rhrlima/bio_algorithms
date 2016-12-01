import math
import random
import sys

#problemas
sys.path.append('../../problems/tsp')
import tsp

problem = tsp #

problem.read_instance("../../problems/tsp/instances/att48.tsp")

CROMOSSOME_SIZE = problem.NUM_POINTS
POPULATION_SIZE = 10


def create_population(population_size):
    aux = []
    for i in range(population_size):
        aux.append(problem.create_solution())
    return aux


def calculate_fitness(cromossome):
    return problem.evaluate_solution(cromossome)


def executar():
    population = create_population(5)
    for cromossomo in population:
        print(calculate_fitness(cromossomo))

executar()
