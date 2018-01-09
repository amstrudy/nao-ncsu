# This Python script creates a bunch of test maps of varying number, size, and density.
# The output is to a .csv file.

import cv2
import numpy
import random
import time
import csv

import oop_a_star as aStar

MAP_SIZE_MIN = 5 # 3 x 3 is smallest map
MAP_SIZE_MAX = 10 # 10 x 10 is biggest map
NUM_TESTS = 10 # number of tests per map size
DENSITY = 0.1 # % map populated with obstacles

class Map:

    def __init__(self, x, y, trial_num):
        self.x = x
        self.y = y
        self.trial_num = trial_num
        self.state = None
        self.time = 0
        self.array = [[None for a in range(y)] for b in range(x)]

def generate_map (i, trial_num): # return Map object
    m = Map(i, i, trial_num) # create empty array i x i
    for j in list(range(m.x)):
        for k in list(range(m.y)):
            m.array[j][k] = numpy.random.choice(numpy.arange(0, 2), p=[1-DENSITY, DENSITY]) # pick either 0 or 1 with certain distribution
    return m

##### GENERATE MAPS #####
maps = [[None for y in range(NUM_TESTS)] for x in range(MAP_SIZE_MAX - MAP_SIZE_MIN + 1)] # make [MAP_SIZE_MAX - MAP_SIZE_MIN + 1][NUM_TESTS]

for i in range(len(maps)):
    for m in range(len(maps[i])):
        maps[i][m] = generate_map(MAP_SIZE_MIN + i, m)

##### RUN A STAR #####

for i in range(len(maps)):
    for j in range(len(maps[i])):
        found_spot = False
        x = 0
        y = 0
        while found_spot == False:
            x = random.randint(0, maps[i][j].x - 1)
            y = random.randint(0, maps[i][j].y - 1)
            if x != 1 and y != 1:
                found_spot = True
        start = time.time()
        ret = aStar.a_star((0, 0), (x - 1, y - 1), maps[i][j].array)
        end = time.time()
        if ret == 0:
            maps[i][j].state = "Fail"
        else:
            maps[i][j].state = "Success"
        maps[i][j].time = end - start
        print(ret, maps[i][j].time)

##### FORMAT DATA #####

formatted_all = [["Trial Number", "X", "Y", "Time (s)", "State"]]
formatted_successes = [["Trial Number", "X", "Y", "Time (s)", "Time (ms)"]]

for i in range(len(maps)):
    for j in range(len(maps[0])):
        formatted_all.append([maps[i][j].trial_num, maps[i][j].x, maps[i][j].y, maps[i][j].time, maps[i][j].state])
        if maps[i][j].state == "Success":
            formatted_successes.append([maps[i][j].trial_num, maps[i][j].x, maps[i][j].y, maps[i][j].time, maps[i][j].time * 1000])

##### PUT INTO CSV #####

myFile = open("All_Data.csv", "w")
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(formatted_all)

myFile = open("Successes.csv", "w")
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(formatted_successes)

print("Writing complete")
