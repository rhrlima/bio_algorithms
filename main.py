import sys

#Appending problems
sys.path.append('problems/tsp')
sys.path.append('problems/rosenbrock')

#Appending algorithms
sys.path.append('algorithms/ga')
sys.path.append('algorithms/sia')
sys.path.append('algorithms/pso')

#Importing problems
import tsp

#Importing algorithms
import ga
import sia
import pso

#Reading the instance for the problem
tsp.read_instance("problems/tsp/instances/test10.tsp")

#Setting the problem to the algorithm
"""
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
"""

import rosenbrock

#rosenbrock.set_dimensions(5)

print("Executing PSO")
pso.set_problem(rosenbrock)
swarm = pso.execute()

for p in swarm:
	print(p.position)
