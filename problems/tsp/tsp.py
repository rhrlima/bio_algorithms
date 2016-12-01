import copy
import math
import random
import re

NAME = ""
DESC = ""
NUM_POINTS = 0
points = []


class Ponto:
    def __init__(self, id, x, y):
        self.id = id
        self.x = int(x)
        self.y = int(y)


def read_instance(archive):
    global NAME, DESC, NUM_POINTS
    #SOURCE_PATH = "instances/"
    file = open(archive)
    NAME = file.readline().replace("\n", "").replace(" ", "").split(":")[1]
    DESC = file.readline().replace("\n", "").replace(" ", "").split(":")[1]
    file.readline() #nao usado
    NUM_POINTS = int(file.readline().replace("\n", "").replace(" ", "").split(":")[1])
    file.readline() #nao usado
    file.readline() #nao usado
    for ponto in range(NUM_POINTS):
        line = file.readline().replace("\n", "")
        points.append(Ponto(line.split(",")[0], line.split(",")[1], line.split(",")[2]))
    #return NAME, DESC, NUM_POINTS, points


def create_solution():
    solution = copy.deepcopy(points)
    random.shuffle(solution)
    return solution


def evaluate_solution(solution):
    fitness = 0
    size = len(solution)
    for i in range(size-1):
        fitness += euclidean_distance(solution[i], solution[i+1])
    fitness += euclidean_distance(solution[size-1], solution[0])
    return fitness


def euclidean_distance(ponto_a, ponto_b):
    return math.sqrt(math.pow(ponto_a.x - ponto_b.x, 2) + math.pow(ponto_a.y - ponto_b.y, 2))
