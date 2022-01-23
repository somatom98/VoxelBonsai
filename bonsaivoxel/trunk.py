import math
import random
from operator import add, sub

import numpy as np

from point import Point
from treeConstants import *
from treeSize import treeSizes


class Trunk:

    def __init__(self, size, species, style):
        self.size = size
        self.species = species
        self.style = style

        self.width = math.ceil(treeSizes[self.size].width)
        self.depth = math.ceil(treeSizes[self.size].depth)
        self.minHeight = math.ceil(treeSizes[self.size].minHeight)
        self.maxHeight = math.ceil(treeSizes[self.size].maxHeight)
        print("Min height:", self.minHeight)
        print("Max height:", self.maxHeight)

        self.generateTrunk()
        self.fillTrunkMatrix()

    def generateTrunk(self):
        self.startingPoint = self.calculateStartingPoint()
        self.endingPoint = self.calculateEndingPoint()
        self.baseWidth = self.calculateBaseWidth()
        print("Base width:", self.baseWidth)

    def calculateStartingPoint(self):
        if self.style in [TreeStyles.BROOM, TreeStyles.FORMAL_UPRIGHT, TreeStyles.INFORMAL_UPRIGHT,
                          TreeStyles.SEMI_CASCADE, TreeStyles.LITERATI, TreeStyles.MULTIPLE_TRUNK]:
            return Point(self.width/2, self.depth/2, 0)
        else:
            #TODO
            return Point(self.width / 2, self.depth / 2, 0)

    def calculateEndingPoint(self):
        if self.style in [TreeStyles.SLANTING, TreeStyles.LITERATI]:
            endingPointZ = self.startingPoint.z + random.uniform(self.minHeight,self.maxHeight)
            return Point(self.startingPoint.x, self.startingPoint.y, endingPointZ).neighborhood2Dz(self.width/2)
        elif self.style in [TreeStyles.CASCADE, TreeStyles.SEMI_CASCADE]:
            operations = (add, sub)
            addOrSubtract = random.choice(operations)
            endingPointX = addOrSubtract(self.startingPoint.x, random.uniform(self.minHeight,self.maxHeight))
            endingPointZ = self.startingPoint.z - random.uniform(self.minHeight, self.maxHeight)
            return Point(endingPointX, self.startingPoint.y, endingPointZ)
        elif self.style in [TreeStyles.FORMAL_UPRIGHT, TreeStyles.INFORMAL_UPRIGHT, TreeStyles.BROOM]:
            endingPointZ = self.startingPoint.z + random.uniform(self.minHeight,self.maxHeight)
            return Point(self.startingPoint.x, self.startingPoint.y, endingPointZ)
        else:
            return self.startingPoint

    def calculateBaseWidth(self):
        if self.style in [TreeStyles.LITERATI]:
            return random.uniform(1, int(self.width/5) + 1) / 2
        else:
            return random.uniform(1, int(self.width/2) + 1) / 2

    def fillTrunkMatrix(self):
        i = TreeParts.TRUNK.value
        print("Starting point:", self.startingPoint.x, self.startingPoint.y, self.startingPoint.z)
        print("Ending point:", self.endingPoint.x, self.endingPoint.y, self.endingPoint.z)
        self.changeCoordinatesToAvoidNegativeIndexes()
        print("Starting point:", self.startingPoint.x, self.startingPoint.y, self.startingPoint.z)
        print("Ending point:", self.endingPoint.x, self.endingPoint.y, self.endingPoint.z)
        matrixSize = self.calculateMatrixSize()
        self.trunkMatrix = np.zeros((matrixSize.z, matrixSize.y, matrixSize.x), dtype=int)
        self.trunkMatrix[self.startingPoint.zInt()][self.startingPoint.yInt()][self.startingPoint.xInt()] = i
        self.trunkMatrix[self.endingPoint.zInt()][self.endingPoint.yInt()][self.endingPoint.xInt()] = 5

    def changeCoordinatesToAvoidNegativeIndexes(self):
        offset = Point(0,0,0)
        if self.endingPoint.hasNegativeCoordinates():
            offset = self.endingPoint.getNegativeOffset()
        if offset.x != 0 or offset.y != 0 or offset.z != 0:
            self.startingPoint = Point(self.startingPoint.x + offset.x, self.startingPoint.y + offset.y, self.startingPoint.z + offset.z)
            self.endingPoint = Point(self.endingPoint.x + offset.x, self.endingPoint.y + offset.y, self.endingPoint.z + offset.z)

    def calculateMatrixSize(self):
        x = max(self.startingPoint.xInt(), self.endingPoint.xInt()) + 1
        y = self.depth
        z = max(self.startingPoint.zInt(), self.endingPoint.zInt()) + 1
        print("Matrix size:",x,y,z)
        return Point(x,y,z)