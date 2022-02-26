import math
import random
import numpy as np


class Point:
    def __init__(self, x, y, z, live=True):
        self.x = x
        self.y = y
        self.z = z
        self.live = live

    @staticmethod
    def fromSpherical(sPoint):
        return Point(sPoint.rho * math.sin(sPoint.theta) * math.cos(sPoint.phi),
                     sPoint.rho * math.sin(sPoint.theta) * math.sin(sPoint.phi),
                     sPoint.rho * math.scosin(sPoint.theta),
                     sPoint.live)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z, self.live)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z, self.live)

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
        point = Point(random.uniform(-r, r), random.uniform(-r, r), random.uniform(-r, r))
        while self.distanceTo(point) >= r:
            point = Point(random.uniform(-r, r), random.uniform(-r, r), random.uniform(-r, r))
        return point

    def neighborhood2Dz(self, r):
        point = Point(random.uniform(-r, r), random.uniform(-r, r), self.z)
        while self.distanceTo(point) >= r:
            point = Point(random.uniform(-r, r), random.uniform(-r, r), self.z)
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


class SphericalPoint:
    def __init__(self, rho, theta, phi, live=True):
        self.rho = rho
        self.theta = theta
        self.phi = phi
        self.live = live

    @staticmethod
    def fromCartesian(cartesianPoint: Point):
        return SphericalPoint(cartesianPoint.distanceTo(Point(0, 0, 0)),
                              math.acos(cartesianPoint.z / cartesianPoint.distanceTo(Point(0, 0, 0))),
                              math.atan(cartesianPoint.y / cartesianPoint.x), cartesianPoint.live)
