# A * Search Algorithm Test

# make steps into groups of pixels that can be travelled across diagonally

import cv2
import numpy as np
import sys

from ast import literal_eval as make_tuple

map_img = cv2.imread("test.png")
map_img = cv2.cvtColor(map_img,cv2.COLOR_RGB2GRAY)
home = make_tuple(sys.argv[1])
goal = make_tuple(sys.argv[2])
step = 0.2 # m

print(map_img)

print(home, goal)

def aStar (home, goal):

    fringe = [] # new queue
    fringe.append(home)
    alreadyVisited = []
    print(fringe)

    while not fringe.empty():
        actions = fringe.pop()

        if node == goal: # check if you are at the end (the goal)
            return listOfActions # return the list of directions for pacman

        alreadyVisited.append(node) # add where you tried to go to the alreadyVisited

        for getNextNode(node):
            if not node in alreadyVisited:
                fringe.push(node)

def gScore (node, goal):
    manhattan_dist = (goal[1] - node[1]) + (goal[0] - node[0])
    return manhattan_dist

def hScore (node, goal):
    manhattan_dist = (goal[1] - node[1]) + (goal[0] - node[0])
    return manhattan_dist

def fScore (node, goal):
    return gScore(node, goal) + hScore(node, goal)

def getNextNode(node):
    # how to do this??

def findMin(listy):
    min_node = listy[0]
    for node in listy:
        if getCostOfActions(node) < getCostOfActions(min_node):
            min_node = node
    return min_node

aStar(home, goal)


def A*(start, goal)
    # The set of nodes already evaluated
    closedSet = []

    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    openSet = [home]

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    cameFrom = []

    # For each node, the cost of getting from the start node to that node.
    gScore []

    # The cost of going from start to start is zero.
    gScore[home] = 0

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    fScore = []

    # For the first node, that value is completely heuristic.
    fScore.append = getCostOfActions(home, goal)

    while openSet is not empty
        current = findMin(openSet) # the node in openSet having the lowest fScore[] value
        if current is goal:
            cameFrom.append(current)
            return cameFrom

        openSet.pop(current) # since current isn't the goal, put current into the already visited set and find the next node
        closedSet.append(current)

        # how to determine neighbor!!

        for neighbor in current
            if neighbor in closedSet
                pass		# Ignore the neighbor which is already evaluated.

            if neighbor not in openSet	# Discover a new node
                openSet.append(neighbor)

            # The distance from start to a neighbor
            tentative_gScore = gScore(home, current) + gScore(current, neighbor)
            if tentative_gScore >= gScore(neighbor, goal)
                continue		# This is not a better path.

            # This path is the best until now. Record it!
            cameFrom[neighbor] = current
            fScore.append(fScore(neighbor, goal))

    return failure
