import math
import random
import sys

POPULATION_SIZE = 100   #Tamanho population
SELECTION_SIZE = 5      #Numero de selecionados
NUM_CLONES = 3          #Numero de clones
MUTATION_RATE = 0.5     #Intesidade de hipermutacao
NUM_NEW = 3             #Numero de novos anti corpos a serem gerados
EVALUATIONS = 100000    #Numero de avaliações


class Antibody:
    def __init__(self, genes, afinity, norm_afinity):
        self.genes = genes
        self.afinity = afinity
        self.norm_afinity = norm_afinity

    def copy(self):
        return Antibody(self.genes[:], self.afinity, self.norm_afinity)


def set_problem(p):
    global problem, ANTIBODY_SIZE
    problem = p
    ANTIBODY_SIZE = problem.NUM_POINTS


def create_population(population_size):
    population = []
    for i in range(population_size):
        population.append(Antibody(problem.create_solution(), -1, -1))
    return population


def evaluate_population(population):
    for antibody in population:
        evaluate_solution(antibody)


def evaluate_solution(antibody):
    antibody.afinity = problem.evaluate_solution(antibody.genes)


def normalize_afinity(population):
    min = max = population[0].afinity

    for antibody in population:
        if antibody.afinity > max:
            max = antibody.afinity
        if antibody.afinity < min:
            min = antibody.afinity

    for antibody in population:
        if (max - min > 0):
            antibody.norm_afinity = (antibody.afinity - min) / (max - min)
        else:
            antibody.norm_afinity = (antibody.afinity - min)


def select_best(population):
    best = []
    population.sort(key = lambda ac: ac.afinity)
    for i in range(SELECTION_SIZE):
        best.append(population[i])
    return best


def clone(best):
    clones = []
    for i in range(SELECTION_SIZE):
        num_clones = int(NUM_CLONES * SELECTION_SIZE / (i+1))
        for clone in range(num_clones):
            clones.append(best[i].copy())
    return clones


def hypermutation(clones):
    for clone in clones:
        hyp_rate = math.exp(-MUTATION_RATE * clone.norm_afinity)
        if random.uniform(0, 1) < hyp_rate:
            while(True):
                r1 = random.randint(0, ANTIBODY_SIZE-1)
                r2 = random.randint(0, ANTIBODY_SIZE-1)
                if r1 != r2: break
            aux = clone.genes[r1]
            clone.genes[r1] = clone.genes[r2]
            clone.genes[r2] = aux


def replace_worst(population, clones):
    best_clones = select_best(clones)
    for i in range(SELECTION_SIZE):
        population[POPULATION_SIZE - i - 1] = best_clones[i]
    population_aux = create_population(NUM_NEW)
    evaluate_population(population_aux)
    for i in range(NUM_NEW):
        population[POPULATION_SIZE - SELECTION_SIZE - i - 1] = population_aux[i]


def init_progress():
    global evaluations
    evaluations = POPULATION_SIZE


def update_progress():
    global evaluations
    evaluations += POPULATION_SIZE


def execute():

    population = create_population(POPULATION_SIZE)
    evaluate_population(population)
    init_progress()
    while(evaluations < EVALUATIONS):
        normalize_afinity(population)
        selected = select_best(population)
        clones = clone(selected)
        hypermutation(clones)
        evaluate_population(clones)
        replace_worst(population, clones)
        update_progress()
    return population
