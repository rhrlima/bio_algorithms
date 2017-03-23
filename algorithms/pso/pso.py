import random

SWARM_SIZE = 10
MAX_EVALUATIONS = 1000

C1 = 2.0
C2 = 2.0
GLOBAL_BEST = []

problem = None

class Particle:

	def __init__(self, pos, fitness):
		self.position = pos
		self.best_pos = pos
		self.velocity = [0 for i in range(len(pos))]
		self.fitness = -1


def set_problem(p):
	global problem
	problem = p


def create_swarm():

	return [Particle(problem.create_solution(), -1) for i in range(SWARM_SIZE)]


def evaluate_particle(particle):

	particle.fitness = problem.evaluate_solution(particle.position)


def evaluate_swarm(swarm):

	[evaluate_particle(particle) for particle in swarm]


def update_velocity(particle):
	vel = particle.velocity
	pos = particle.position
	p_best = particle.best_pos
	g_best = GLOBAL_BEST
	for index in range(len(particle.velocity)):
		r1 = random.uniform(0, 1)
		r2 = random.uniform(0, 1)
		vel[index] = vel[index] + C1 * r1 * (p_best[index] - pos[index]) + C2 * r2 * (g_best[index] - pos[index])


def update_position(particle):
	for index in len(particle.position):
		particle.position[index] += particle.velocity[index]


def apply_mutation(particle):

	pass


def update_local_best(particle):

	pass


def update_global_best(particle):

	pass


def init_progress():
    global evaluations
    evaluations = SWARM_SIZE


def update_progress():
    global evaluations
    evaluations += SWARM_SIZE


def execute():
	swarm = create_swarm()
	evaluate_swarm(swarm)
	init_progress()
	while(evaluations < MAX_EVALUATIONS):
		for particle in swarm:
			update_local_best(particle)
			update_global_best(particle)
			update_velocity(particle)
			update_position(particle)
			apply_mutation(particle)
			evaluate_particle(particle)
			update_local_best(particle)
			update_global_best(particle)
		update_progress()
	return swarm