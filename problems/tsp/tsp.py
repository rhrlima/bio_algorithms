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
        fitness += euclidean_distance(solution[i], solution[i+1])
    fitness += euclidean_distance(solution[size-1], solution[0])
    return fitness


def euclidean_distance(ax, ay, bx, by):
    return math.sqrt(math.pow(points[pa]['x'] - points[pb]['x'], 2) + math.pow(points[pa]['y'] - points[pb]['y'], 2))
