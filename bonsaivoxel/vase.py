import math

import numpy as np

from treeConstants import *
from treeSize import treeSizes
from treeStyle import treeStyles


class Vase:
    def __init__(self, compatibleTreeSize, compatibleTreeSpecies, compatibleTreeStyles, vaseMatrix):
        self.compatibleTreeSize = compatibleTreeSize
        self.compatibleTreeSpecies = compatibleTreeSpecies
        self.compatibleTreeStyles = compatibleTreeStyles
        self.vaseMatrix = vaseMatrix

i = TreeParts.VASE.value
vases = [
    Vase(TreeSizes.MAME,
         [TreeSpecies.MAPLE, TreeSpecies.RED_MAPLE],
         [TreeStyles.BROOM, TreeStyles.FORMAL_UPRIGHT, TreeStyles.INFORMAL_UPRIGHT, TreeStyles.SLANTING, TreeStyles.CASCADE,
          TreeStyles.SEMI_CASCADE, TreeStyles.LITERATI, TreeStyles.MULTIPLE_TRUNK, TreeStyles.FOREST],
         np.array([[[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i]]])
         ),
    Vase(TreeSizes.MAME,
         [TreeSpecies.JUNIPER, TreeSpecies.TAXUS, TreeSpecies.BLACK_PINE, TreeSpecies.WHITE_PINE],
         [TreeStyles.BROOM, TreeStyles.FORMAL_UPRIGHT, TreeStyles.INFORMAL_UPRIGHT, TreeStyles.SLANTING, TreeStyles.CASCADE,
          TreeStyles.SEMI_CASCADE, TreeStyles.LITERATI, TreeStyles.MULTIPLE_TRUNK, TreeStyles.FOREST],
         np.array([[[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i]],
          [[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i]]])
         )
]

def getCompatibleVases(treeSize, treeSpecies, treeStyle):
    compatibleVasesMatrixes = list()
    for vase in vases:
        if treeSize == vase.compatibleTreeSize:
            compatibleTreeSpeciesFound = False
            for compatibleTreeSpecies in vase.compatibleTreeSpecies:
                if treeSpecies == compatibleTreeSpecies:
                    compatibleTreeSpeciesFound = True
                    break
            if compatibleTreeSpeciesFound:
                compatibleVasesMatrixes.append(vase.vaseMatrix)
    return compatibleVasesMatrixes

def getDefaultVase(tree):
    width = treeSizes[tree.size].width * treeStyles[tree.style].widthFactor
    depth = treeSizes[tree.size].depth * treeStyles[tree.style].widthFactor
    return np.ones((1, math.ceil(depth), math.ceil(width)), dtype=int)