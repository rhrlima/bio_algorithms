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
import rosenbrock

#Importing algorithms
import ga
import sia
import pso

#Reading the instance for the problem
tsp.read_instance("problems/tsp/instances/test10.tsp")

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


print("Executing PSO")
pso.set_problem(rosenbrock)
for i in range(30):
	swarm = pso.execute()
	swarm.sort(key = lambda p: p.fitness)
	print("Final best:", swarm[0].fitness)
