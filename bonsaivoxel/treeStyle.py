from treeConstants import *


class TreeStyle:
    def __init__(self, name, minWidthFactor = 1, maxWidthFactor = 1, minHeightFactor = 1, maxHeightFactor = 1, middlePointsDeviation = 1):
        self.name = name
        self.minWidthFactor = minWidthFactor
        self.maxWidthFactor = maxWidthFactor
        self.minHeightFactor = minHeightFactor
        self.maxHeightFactor = maxHeightFactor
        self.middlePointsDeviation = middlePointsDeviation

treeStyles = {
    TreeStyles.BROOM: TreeStyle("Broom"),
    TreeStyles.FORMAL_UPRIGHT: TreeStyle("Formal Upright", maxHeightFactor = 2),
    TreeStyles.INFORMAL_UPRIGHT: TreeStyle("Informal Upright"),
    TreeStyles.SLANTING: TreeStyle("Slanting", minWidthFactor = 2, maxWidthFactor = 2),
    TreeStyles.CASCADE: TreeStyle("Cascade", minWidthFactor = 2, maxWidthFactor = 2, minHeightFactor = 0.5, maxHeightFactor = 0.5),
    TreeStyles.SEMI_CASCADE: TreeStyle("Semicascade", minWidthFactor = 1.5, maxWidthFactor = 1.5),
    TreeStyles.LITERATI: TreeStyle("Literati", minWidthFactor = 0.5, maxWidthFactor = 0.5, minHeightFactor = 2, maxHeightFactor = 2),
    TreeStyles.MULTIPLE_TRUNK: TreeStyle("Multiple Trunk"),
    TreeStyles.FOREST: TreeStyle("Forest")
}