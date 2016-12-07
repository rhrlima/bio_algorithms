import copy
import math
import random
import re

NAME = ""
DESC = ""
NUM_POINTS = 0
points = {}


def read_instance(archive):
    global NAME, DESC, NUM_POINTS
    file = open(archive)
    NAME = file.readline().replace("\n", "").replace(" ", "").split(":")[1]
    DESC = file.readline().replace("\n", "").replace(" ", "").split(":")[1]
    file.readline() #nao usado
    NUM_POINTS = int(file.readline().replace("\n", "").replace(" ", "").split(":")[1])
    file.readline() #nao usado
    file.readline() #nao usado
    for point in range(NUM_POINTS):
        line = file.readline().replace("\n", "")
        points[line.split(",")[0]] = {'x':int(line.split(",")[1]), 'y':int(line.split(",")[2])}


def create_solution():
    solution = []
    for key in points.keys():
        solution.append(key)
    random.shuffle(solution)
    return solution


def evaluate_solution(solution):
    fitness = 0
    size = len(solution)
    for i in range(size-1):
        ax = points[solution[i]]['x']
        bx = points[solution[i+1]]['x']
        ay = points[solution[i]]['y']
        by = points[solution[i+1]]['y']
        fitness += euclidean_distance(ax, ay, bx, by)#solution[i], solution[i+1])
    ax = points[solution[size-1]]['x']
    bx = points[solution[0]]['x']
    ay = points[solution[size-1]]['y']
    by = points[solution[0]]['y']
    fitness += euclidean_distance(ax, ay, bx, by)
    return fitness


def euclidean_distance(ax, ay, bx, by):
    return math.sqrt(math.pow(ax-bx, 2) + math.pow(bx-by, 2))
