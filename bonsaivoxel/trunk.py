import math
import random
from operator import add, sub

import numpy as np

from point import Point, SphericalPoint
from treeConstants import *
from treeSize import treeSizes


class Trunk:

    def __init__(self, size, species, style):
        self.size = size
        self.species = species
        self.style = style
        self.points = {}

        self.width = math.ceil(treeSizes[self.size].width)
        self.depth = math.ceil(treeSizes[self.size].depth)
        self.minHeight = math.ceil(treeSizes[self.size].minHeight)
        self.maxHeight = math.ceil(treeSizes[self.size].maxHeight)
        print("Min height:", self.minHeight)
        print("Max height:", self.maxHeight)

        self.generateTrunk()
        self.fillTrunkMatrix()

    def addEdge(self, vrtx1, vrtx2):
        if vrtx1 in self.points:
            self.points[vrtx1].append(vrtx2)
        else:
            self.points[vrtx1] = [vrtx2]

    def findEdges(self):
        edgename = []
        for vrtx in self.points:
            for nxtvrtx in self.points[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def generateTrunk(self):
        startingPoint = self.calculateStartingPoint()
        endingPoint = self.calculateEndingPoint(startingPoint)
        self.generateTrunkGraph(startingPoint, endingPoint)
        self.baseWidth = self.calculateBaseWidth()
        print("Base width:", self.baseWidth)

    def calculateStartingPoint(self):
        if self.style in [TreeStyles.BROOM, TreeStyles.FORMAL_UPRIGHT, TreeStyles.INFORMAL_UPRIGHT,
                          TreeStyles.SEMI_CASCADE, TreeStyles.LITERATI, TreeStyles.MULTIPLE_TRUNK]:
            return Point(self.width/2, self.depth/2, 0)
        else:
            #TODO
            return Point(self.width / 2, self.depth / 2, 0)

    def calculateEndingPoint(self, startingPoint):
        if self.style in [TreeStyles.SLANTING, TreeStyles.LITERATI]:
            endingPointZ = startingPoint.z + random.uniform(self.minHeight,self.maxHeight)
            return Point(startingPoint.x, startingPoint.y, endingPointZ).neighborhood2Dz(self.width/2)
        elif self.style in [TreeStyles.CASCADE, TreeStyles.SEMI_CASCADE]:
            operations = (add, sub)
            addOrSubtract = random.choice(operations)
            endingPointX = addOrSubtract(startingPoint.x, random.uniform(self.minHeight,self.maxHeight))
            endingPointZ = startingPoint.z - random.uniform(self.minHeight, self.maxHeight)
            return Point(endingPointX, startingPoint.y, endingPointZ)
        elif self.style in [TreeStyles.FORMAL_UPRIGHT, TreeStyles.INFORMAL_UPRIGHT, TreeStyles.BROOM]:
            endingPointZ = startingPoint.z + random.uniform(self.minHeight,self.maxHeight)
            return Point(startingPoint.x, startingPoint.y, endingPointZ)
        else:
            return startingPoint

    def generateTrunkGraph(self, startingPoint, endingPoint):
        pointA, pointB = startingPoint, endingPoint
        while self.canGenerateMiddlePoint(pointA, pointB):
            pointB = self.generateMiddlePoint(pointA, pointB)
            self.addEdge(pointA, pointB)
            pointA, pointB = pointB, endingPoint
        self.addEdge(pointA, pointB)
        print("edge:",
              "[", pointA.x, ",", pointA.y, ",", pointA.z, "]",
              "[", pointB.x, ",", pointB.y, ",", pointB.z, "]")

    def generateMiddlePoint(self, pointA, pointB):
        ANGLE_VARIATION = 45
        middlePoint = pointB
        if self.style in [TreeStyles.INFORMAL_UPRIGHT, TreeStyles.SLANTING, TreeStyles.CASCADE, TreeStyles.SEMI_CASCADE, TreeStyles.LITERATI]:
            pointBUsingAAsOrigin = pointB - pointA
            sphPointB = SphericalPoint.fromCartesian(pointBUsingAAsOrigin)
            sphMiddlePoint = SphericalPoint(sphPointB.rho/3,
                                            sphPointB.theta + random.uniform(-ANGLE_VARIATION, ANGLE_VARIATION),
                                            sphPointB.phi + random.uniform(-ANGLE_VARIATION, ANGLE_VARIATION),
                                            sphPointB.live)
            middlePoint = Point.fromSpherical(sphMiddlePoint)
        return middlePoint
        #TreeStyles.BROOM, TreeStyles.MULTIPLE_TRUNK, TreeStyles.FOREST

    def canGenerateMiddlePoint(self, pointA, pointB):
        return self.style not in [TreeStyles.FORMAL_UPRIGHT] and pointA.distanceTo(pointB) >= 1

    def calculateBaseWidth(self):
        if self.style in [TreeStyles.LITERATI]:
            return random.uniform(1, int(self.width/5) + 1) / 2
        else:
            return random.uniform(1, int(self.width/2) + 1) / 2

    def fillTrunkMatrix(self): #TODO
        i = TreeParts.TRUNK.value
        self.changeCoordinatesToAvoidNegativeIndexes()
        for point in self.points:
            print("Point:", point.x, point.y, point.z)
        matrixSize = self.calculateMatrixSize()
        self.trunkMatrix = np.zeros((matrixSize.z, matrixSize.y, matrixSize.x), dtype=int)
        #self.trunkMatrix[self.startingPoint.zInt()][self.startingPoint.yInt()][self.startingPoint.xInt()] = i
        #self.trunkMatrix[self.endingPoint.zInt()][self.endingPoint.yInt()][self.endingPoint.xInt()] = 5

    def changeCoordinatesToAvoidNegativeIndexes(self):
        offset = Point(0,0,0)
        for point in self.points:
            if point.hasNegativeCoordinates():
                newOffset = point.getNegativeOffset()
                offset = Point(max(offset.x, newOffset.x), max(offset.y, newOffset.y), max(offset.z, newOffset.z))
        if offset.x != 0 or offset.y != 0 or offset.z != 0:
            for point in self.points:
                point = Point(point.x + offset.x, point.y + offset.y, point.z + offset.z)

    def calculateMatrixSize(self): #TODO
        #x = max(self.startingPoint.xInt(), self.endingPoint.xInt()) + 1
        y = self.depth
        #z = max(self.startingPoint.zInt(), self.endingPoint.zInt()) + 1
        print("Matrix size:",x,y,z)
        return Point(x,y,z)