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

class Node:

    def __init__ (self, home=(0,0), goal=(1,1), location=(0,0)):
        self.location
        self.home = home
        self.goal = goal
        self.neighbors = []
        self.gScore = self.gScore(self.home, self.location)
        self.hScore = self.hScore()
        self.fScore = self.gScore + self.hScore

    def gScore (self):
        manhattan_dist = (self.goal[1] - self.home[1]) + (self.goal[0] - self.home[0])
        return manhattan_dist

    def hScore (self):
        manhattan_dist = (self.goal[1] - self.location[1]) + (self.goal[0] - self.location[0])
        return manhattan_dist

    def generateNeighbors ():
        neighbors = []
        if self.location[0] + 1 < len(map_img[0]):
            neighbors.append(Node(self.home, self.goal, (self.location[0] + 1, self.location[1])))
        if self.location[0] - 1 >= 0:
            neighbors.append(Node(self.home, self.goal, (self.location[0] - 1, self.location[1])))
        if self.location[1] + 1 < len(map_img)
            neighbors.append(Node(self.home, self.goal, (self.location[0], self.location[1] + 1)))
        if self.location[1] - 1 >= 0:
            neighbors.append(Node(self.home, self.goal, (self.location[0] self.location[1] - 1)))
        self.neighbors = neighbors

def isNotIn (neighbor, listy):
    for i in listy:
        if neighbor is i:
            return True
    return False

def a_star ():
    # create the fringe and alreadyVisited lists
    fringe = []
    alreadyVisited = []
    listOfActions = []

    # create node object for home
    home_node = Node(home, goal, home)

    # add home as first element of fringe
    fringe.append(home_node)
    listOfActions.append(home_node.location)

    while not fringe.empty():
        cur_node = listOfActions[-1] # expand on last best node
        if cur_node.location == goal:
            print("Made it to the goal!")
            return listOfActions
        cur_node.generateNeighbors() # make new nodes to check
        for neighbor in cur_node.neighbors:
            if neightbor isNotIn(neighbor, alreadyVisited): # make sure you haven't already checked that node
                fringe.append(neighbor)
            if neighbor.fScore > cur_node.fScore: # if score is higher, this path is not better thusc continue without saving this node
                alreadyVisited.append(neighbor)
                break
            listOfActions.append(neighbor) # if score is better, save this as part of your path


aStar()
