import math
import random
import sys
sys.path.append('../../problems/tsp')
import tsp

problem = tsp
instance_name = sys.argv[1]
problem.read_instance("../../problems/tsp/instances/" + instance_name)

CROMOSSOME_SIZE = problem.NUM_POINTS
POPULATION_SIZE = 100
MAX_EVALUATIONS = 100000
SELECTION_SIZE = 2
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.05


class Cromossome:
    def __init__(self, genes, fitness):
        self.genes = genes;
        self.fitness = fitness


def create_population(population_size):
    population = []
    for i in range(population_size):
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
    offspring = Cromossome(parents[0].genes[:], -1)
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
    return offspring


def replacement(population, offspring):
    worst = population[0]
    for cromossome in population:
        if cromossome.fitness > worst.fitness:
            worst = cromossome
    population.remove(worst)
    population.append(Cromossome(offspring.genes, offspring.fitness))
    return population


def init_progress():
    global evaluations
    evaluations = POPULATION_SIZE


def update_progress():
    global evaluations
    evaluations += POPULATION_SIZE


def executar():
    population = create_population(POPULATION_SIZE)
    evaluate_population(population)
    init_progress()
    while(evaluations < MAX_EVALUATIONS):
        parents = select_parents(population)
        offspring = apply_crossover(parents)
        offspring = apply_mutation(offspring)
        evaluate_solution(offspring)
        population = replacement(population, offspring)
        #population.sort(key = lambda c: c.fitness)
        #print("best: ", population[0].fitness)
        update_progress()
    return population


for i in range(30):
    population = executar()
    population.sort(key = lambda c: c.fitness)
    print("Final best: ", population[0].fitness)
    #print_solution(population[0])
