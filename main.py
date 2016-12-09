import sys

#Appending problems
sys.path.append('problems/tsp')

#Appending algorithms
sys.path.append('algorithms/ga')
sys.path.append('algorithms/sia')

#Importing problems
import tsp

#Importing algorithms
import ga
import sia

#Reading the instance for the problem
tsp.read_instance("problems/tsp/instances/att48.tsp")

#Setting the problem to the algorithm
print("Executing GA")
ga.set_problem(tsp)
for i in range(30):
    #Executing the algorithm
    population = ga.execute()
    population.sort(key = lambda c: c.fitness)
    print("Final best: ", population[0].fitness)

print("Executing SIA")
sia.set_problem(tsp)
for i in range(30):
    #Executing the algorithm
    population = sia.execute()
    population.sort(key = lambda a: a.afinity)
    print("Final best: ", population[0].afinity)
