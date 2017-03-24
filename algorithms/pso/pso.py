import random

SWARM_SIZE = 100
MAX_EVALUATIONS = 100000
C1 = 1.5
C2 = 1.5
MUTATION_RATE = 0.01

GLOBAL_BEST = None
problem = None

class Particle:

	def __init__(self, pos, fitness):
		self.position = pos
		self.best_pos = pos[:]
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
	for index in range(len(particle.position)):
		particle.position[index] += particle.velocity[index]


def apply_mutation(particle):
	rate = random.uniform(0, 1)
	if rate < MUTATION_RATE:
		index = random.randint(0, len(particle.position)-1)
		particle.position[index] = random.uniform(problem.MIN, problem.MAX)


def update_local_best(particle):
	prev_fit = problem.evaluate_solution(particle.best_pos)
	curr_fit = problem.evaluate_solution(particle.position)
	if curr_fit < prev_fit:
		particle.best_pos = particle.position[:]


def update_global_best(particle):
	global GLOBAL_BEST
	if GLOBAL_BEST is None:
		GLOBAL_BEST = particle.position[:]
	else:
		prev_fit = problem.evaluate_solution(GLOBAL_BEST)
		curr_fit = problem.evaluate_solution(particle.position)
		if curr_fit < prev_fit:
			GLOBAL_BEST = particle.position[:]


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
		update_progress()
	return swarm