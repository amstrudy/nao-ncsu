import cv2
import numpy as np
import sys
from Queue import PriorityQueue

from ast import literal_eval as make_tuple

class Node:

    def __init__ (self, home=(0,0), goal=(1,1), location=(0,0), gScore = 0):
        self.location = location
        self.home = home
        self.goal = goal
        self.neighbors = []
        self.gScore = gScore
        self.hScore = self.hScore()
        self.fScore = self.gScore + self.hScore

    def hScore (self):
        manhattan_dist = abs((self.goal[0] - self.location[0])) + abs(self.goal[1] - self.location[1])
        return manhattan_dist

    def generateNeighbors (self, map_img):
        neighbors = []
        if self.location[0] + 1 < len(map_img[0]) and map_img[self.location[0] + 1][self.location[1]] != 1:
            neighbors.append(Node(self.home, self.goal, (self.location[0] + 1, self.location[1]), self.gScore + 1))
        if self.location[0] - 1 >= 0 and map_img[self.location[0] - 1][self.location[1]] != 1:
            neighbors.append(Node(self.home, self.goal, (self.location[0] - 1, self.location[1]), self.gScore + 1))
        if self.location[1] + 1 < len(map_img) and map_img[self.location[0]][self.location[1] + 1] != 1:
            neighbors.append(Node(self.home, self.goal, (self.location[0], self.location[1] + 1), self.gScore + 1))
        if self.location[1] - 1 >= 0 and map_img[self.location[0]][self.location[1] - 1] != 1:
            neighbors.append(Node(self.home, self.goal, (self.location[0], self.location[1] - 1), self.gScore + 1))
        self.neighbors = neighbors

    def __str__ (self):
        return "\n----------\n" + "Location: " + str(self.location) + "\nHome: " + str(self.home) + "\nGoal: " + str(self.goal) + "\nNumber of Neighbors: " + str(len(self.neighbors)) + "\nG Score: " + str(self.gScore) + "\nH Score: " + str(self.hScore) + "\nF Score: " + str(self.fScore) + "\n----------\n"

def isNotIn (neighbor, listy):
    for i in listy:
        if neighbor is i:
            return False
    return True

def printMap ((index1, index2)):
    map_img_cp[index1, index2] = 9
    print(map_img_cp)

def reconstruct(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    return total_path

def a_star(home, goal, map_img):

    # create node object for home
    home_node = Node(home, goal, home)

    # set of nodes already evaluated
    closedSet = set()

    # set of currently discovered nodes that are not evaluated yet
    # initially, only the start node is known
    openSet = set([home_node])
    cameFrom = {}
    count = 0;

    while len(openSet) != 0:
        tempfScore = next(iter(openSet)).fScore
        current = next(iter(openSet))
        for i in iter(openSet):
            if i.fScore < tempfScore:
                tempfScore = i.fScore
                current = i

        if current.location == home_node.goal:
            #print("Made it to goal")
            return reconstruct(cameFrom, current.location)
        openSet.remove(current)
        closedSet.add(current)

        current.generateNeighbors(map_img)
        for neighbor in current.neighbors:

            if count > (len(map_img) * len(map_img[0])):
                return 0

            if neighbor in closedSet:
                continue

            if neighbor not in openSet:
                openSet.add(neighbor)

            if current.gScore+ abs(current.fScore - neighbor.fScore) >= neighbor.gScore:
                continue # this is not eh better path
            # this path is the best for now, so record it
            cameFrom[neighbor.location] = current.location
        #print(current)
        count += 1 # Total number of nodes checked
        #printMap(current.location)
if __name__ == "__main__":

    # map_img = cv2.imread("test.png")
    # map_img = cv2.cvtColor(map_img,cv2.COLOR_RGB2GRAY)
    # for i in range(map_img.shape[0]):
    #     for j in range(map_img.shape[1]):
    #         if map_img[i][j] == 0:
    #             map_img[i][j] = 1
    #         else:
    #             map_img[i][j] = 0
    map_img = [[0, 1, 1, 1, 0],[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
    map_img = np.asarray(map_img)
    map_img_cp = map_img.copy()
    if make_tuple(sys.argv[2])[0] < len(map_img) and make_tuple(sys.argv[2])[0] < len(map_img[0]):
        home = make_tuple(sys.argv[1])
        goal = make_tuple(sys.argv[2])
    else:
        print("Goal out of bounds. Please run again.")
    step = 0.2 # m

    print(map_img)

    print(home, goal)

    print(a_star(home, goal, map_img))
