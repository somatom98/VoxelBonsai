import math
import random
import numpy as np


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def xInt(self):
        return math.floor(self.x)

    def yInt(self):
        return math.floor(self.y)

    def zInt(self):
        return math.floor(self.z)

    def distanceTo(self, otherPoint):
        p1 = np.array([self.x, self.y, self.z])
        p2 = np.array([otherPoint.x, otherPoint.y, otherPoint.z])

        return np.sqrt(np.sum((p1 - p2) ** 2, axis=0))

    def neighborhood3D(self, r):
        point = Point(random.uniform(-r,r), random.uniform(-r,r), random.uniform(-r,r))
        while self.distanceTo(point) >= r:
            point = Point(random.uniform(-r,r), random.uniform(-r,r), random.uniform(-r,r))
        return point

    def neighborhood2Dz(self, r):
        point = Point(random.uniform(-r,r), random.uniform(-r,r), self.z)
        while self.distanceTo(point) >= r:
            point = Point(random.uniform(-r,r), random.uniform(-r,r), self.z)
        return point

    def hasNegativeCoordinates(self):
        return self.x < 0 or self.y < 0 or self.z < 0

    def getNegativeOffset(self):
        xOffset = 0
        yOffset = 0
        zOffset = 0
        if self.x < 0:
            xOffset = -self.xInt()
        if self.y < 0:
            yOffset = -self.yInt()
        if self.z < 0:
            zOffset = -self.zInt()
        return Point(xOffset, yOffset, zOffset)