"""
Created on Sat Nov 14 22:23:58 2020
@author: Grace Michael
DS2000: Programming with Data
@file  : ants.py HW 10
"""
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# Colors
WHITE = 0
RED = 1
BLUE = 2
GREEN = 3
YELLOW = 4
BLACK = 5
color_list = ['white', 'red', 'blue', 'green'] # 'yellow', 'black']

# Directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Turns
STRAIGHT = 0
REVERSE = 2
LEFT = 3
RIGHT = 1


class Ant:

    def __init__(self, x=0, y=0, direction=NORTH):
        """ Construct a new ant at position (x,y)
        and heading in the specified direction (NORTH, SOUTH, EAST, or WEST) """
        self.x = x
        self.y = y
        self.xmax = 0  # world boundary - set when ant is added to world
        self.ymax = 0  # world boundary - set when ant is added to world
        self.direction = direction

    def get_position(self):
        """ Get the x and y position of the ant
        Return a (x,y) tuple """
        return (self.x, self.y)

    def turn(self, t):
        """ Turn either LEFT, RIGHT, or REVERSE direction
        Update ant's direction (NORTH, SOUTH, EAST, WEST) accordingly """
        #the direction is the remainder of the division by 4
        self.direction = (self.direction + t) % 4

    def move(self, steps):
        """ Move in current direction some number of steps.
        Wrap around if the ant goes out of bounds
        Note, when displaying images, (0,0) is in the
        upper left-hand corner.  Increasing x is down (SOUTH)
        and increasing y is to the right (EAST) """
        # divide by remainder to wrap around
        # adding and subrtacing determines the direction
        if self.direction == 0:
            self.x = (self.x - steps) % self.xmax
        if self.direction == 1:
            self.y = (self.y + steps) % self.ymax
        if self.direction == 2:
            self.x = (self.x + steps) % self.xmax
        if self.direction == 3:
            self.y = (self.y - steps) % self.ymax



class World:

    def __init__(self, xmax, ymax):
        """ Create a world. """
        self.xmax = xmax  # X-Boundary
        self.ymax = ymax  # Y-Boundary
        self.world = np.zeros((xmax, ymax), dtype=int)  # World grid
        self.rules = {}  # Rule storage: curr_color -> (next_col, turn, steps)
        self.ants = []   # List of ant objects.

    def add_rule(self, current_color, next_color, turn, steps):
        """ Register a rule with the world.
            If an an ant is at a position with <current_color>,
            then it changes the world to <next_color> at that location,
            then does a specified <turn>, and takes <steps> forward
            Rules should be stored in a dictionary:
                Key = current_color
                Value = (next_color, turn, steps) tuple
        """
        #updates the dictionary
        self.rules[current_color] = next_color, turn, steps

    def add_ant(self, ant):
        """ Add an ant to the world """
        # ants parameter is the same as the size of the world
        ant.xmax = self.xmax
        ant.ymax = self.ymax
        self.ants.append(ant)

        # Store world boundaries with each ant.

        # Add the ant to the internal list of ants

    def move_ant(self, ant):
        """ An ant moves according to some rule, updating the
        state of the world in the process. """
        # Get the current position of the ant
        current_p = ant.get_position()

        # Get the color at that point in the world
        color = self.world[current_p[0]][current_p[1]]

        # Identify the next color, ant's turn, and number
        # of steps based on the color at the ant's current position
        # (i.e., look up the rule that applies!)
        rule = self.rules[color]
        next_color = rule[0]
        turn = rule[1]
        move = rule[2]


        # Update the color at the current position
        self.world[current_p[0]][current_p[1]] = next_color

        # Turn and move the ant

        ant.turn(turn)
        ant.move(move)

    def run(self, iterations, rows=4, cols=4, filename=None):
        """ Move each ant in the world repeatedly
        for some number of move iterations. Then Display
        the state of the world. Repeat until a rows X columns
        grid of image snapshots have been taken.

        iterations = # of times all ants in the world are moved
                     between snapshots

        This method will produce an array of subplots with
        a specified number of rows and cols.

        If filename is provided, it will save the resulting image
        to a .png file

        YES - I implemented this method for you!
        """

        fig = plt.figure(figsize=(8, 8))
        cmap = colors.ListedColormap(color_list)
        for img in range(1, rows * cols + 1):
            for _ in range(iterations):
                for ant in self.ants:
                    self.move_ant(ant)

            fig.add_subplot(rows, cols, img)
            plt.imshow(self.world, cmap=cmap)
            plt.title('N='+str(iterations * img))

        for ax in fig.get_axes():
            ax.label_outer()

        if filename != None:
            plt.savefig(filename)

        plt.show()


def main():

    # Create worlds
    xmax, ymax = 1000, 1000
    world = World(xmax, ymax)

    # Add some rules:  (Current_color, Next_color, Turn, Num_steps)
    world.add_rule(WHITE, RED, RIGHT, 2)
    world.add_rule(RED, BLUE, LEFT, 2)
    world.add_rule(BLUE, GREEN, RIGHT, 2)
    world.add_rule(GREEN, WHITE, LEFT, 2)

    # Create some ants at a random location on the world
    # and moving initially in some random direction
    num_ants = 10
    for _ in range(num_ants):

        # Give each ant a random position
        x = rnd.randint(1,5)
        y = rnd.randint(1,5)

        # and a random direction
        direction = rnd.randint(1,5)

        # Construct the ant
        ant = Ant(x, y, direction)

        # Add the ant to the world
        world.add_ant(ant)

        # Run the world!  Feel free to experiment with these parameters.
    world.run(iterations=300000, rows=3, cols=3, filename='ants.png')


if __name__ == '__main__':
    main()
