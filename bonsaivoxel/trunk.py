import math
import random
from operator import add, sub

import numpy as np
from utils.dataTree import DataTree

from point import Point, SphericalPoint
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
        self.endingPoint = self.calculateEndingPoint(self.startingPoint)
        self.points = DataTree(self.startingPoint)
        self.generateTrunkGraph(self.startingPoint, self.endingPoint)
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
        pointA = startingPoint
        while self.canGenerateMiddlePoint(pointA, endingPoint):
            midPoint = self.generateMiddlePoint(pointA, endingPoint)
            self.points.addEdge(pointA, midPoint)
            pointA = midPoint
        self.points.addEdge(pointA, endingPoint)

    def canGenerateMiddlePoint(self, pointA, pointB):
        return self.style not in [TreeStyles.FORMAL_UPRIGHT] and pointA.distanceTo(pointB) >= 1

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
            middlePoint = middlePoint + pointA
        return middlePoint
        #TreeStyles.BROOM, TreeStyles.MULTIPLE_TRUNK, TreeStyles.FOREST

    def calculateBaseWidth(self):
        if self.style in [TreeStyles.LITERATI]:
            return random.uniform(1, int(self.width/5) + 1) / 2
        else:
            return random.uniform(1, int(self.width/2) + 1) / 2

    def fillTrunkMatrix(self): 
        self.changeCoordinatesToAvoidNegativeIndexes()
        self.initializeTrunkMatrix()
        self.drawTrunk(self.startingPoint)
        self.trunkMatrix[self.startingPoint.zInt()][self.startingPoint.yInt()][self.startingPoint.xInt()] = 0
        self.trunkMatrix[self.endingPoint.zInt()][self.endingPoint.yInt()][self.endingPoint.xInt()] = 0

    def changeCoordinatesToAvoidNegativeIndexes(self):
        offset = self.getNegativeOffset(self.startingPoint)
        offset = Point(offset.xInt(), offset.yInt(), offset.zInt())
        print("Offset:", offset)
        if offset.x != 0 or offset.y != 0 or offset.z != 0:
            self.points.incrementAllNodes(offset)
            self.startingPoint += offset
            self.endingPoint += offset
    
    def getNegativeOffset(self, point):
        print("Point", point)
        offset = Point(max(-point.x + 1, 0), max(-point.y + 1, 0), max(-point.z + 1, 0))
        if self.points.hasNext(point):
            for child in self.points.findNextNodes(point):
                childOffset = self.getNegativeOffset(child)
                return Point(max(offset.x, childOffset.x), max(offset.y, childOffset.y), max(offset.z, childOffset.z))
        else:
            return offset

    def initializeTrunkMatrix(self):
        size = self.getMaxDimensions(self.startingPoint)
        print("Matrix size:", size.xInt(), size.yInt(), size.zInt())
        self.trunkMatrix = np.zeros((size.zInt(), size.yInt(), size.xInt()), dtype=int)
    
    def getMaxDimensions(self, point):
        print("Positive:", point)
        maxDimensions = Point(max(point.x + 1, 0), max(point.y + 1, 0), max(point.z + 1, 0))
        if self.points.hasNext(point):
            for child in self.points.findNextNodes(point):
                childMax = self.getMaxDimensions(child)
                return Point(max(maxDimensions.x, childMax.x), max(maxDimensions.y, childMax.y), max(maxDimensions.z, childMax.z))
        else:
            return maxDimensions
    
    def drawTrunk(self, point):
        if self.points.hasNext(point):
            for child in self.points.findNextNodes(point):
                self.drawTrunk(child)
        self.trunkMatrix[point.zInt(), point.yInt(), point.xInt()] = TreeParts.TRUNK.value
        print("POINT:", point)