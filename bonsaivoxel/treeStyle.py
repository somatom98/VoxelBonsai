from treeConstants import *


class TreeStyle:
    def __init__(self, name, widthFactor, minHeightFactor, maxHeightFactor):
        self.name = name
        self.widthFactor = widthFactor
        self.minHeightFactor = minHeightFactor
        self.maxHeightFactor = maxHeightFactor

treeStyles = {
    TreeStyles.BROOM: TreeStyle("Broom", 1, 1, 1),
    TreeStyles.FORMAL_UPRIGHT: TreeStyle("Formal Upright", 1, 1, 2),
    TreeStyles.INFORMAL_UPRIGHT: TreeStyle("Informal Upright", 1, 1, 1),
    TreeStyles.SLANTING: TreeStyle("Slanting", 2, 1, 1),
    TreeStyles.CASCADE: TreeStyle("Cascade", 2, 0.5, 0.5),
    TreeStyles.SEMI_CASCADE: TreeStyle("Semicascade", 1.5, 1, 1),
    TreeStyles.LITERATI: TreeStyle("Literati", 0.5, 2, 2),
    TreeStyles.MULTIPLE_TRUNK: TreeStyle("Multiple Trunk", 1, 1, 1),
    TreeStyles.FOREST: TreeStyle("Forest", 1, 1, 1)
}