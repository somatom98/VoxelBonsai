from enum import Enum

class TreeSizes(Enum):
    MAME = 1
    SHOHIN = 2
    CHUHIN = 3
    DAI = 4

class TreeSpecies(Enum):
    JUNIPER = 1
    TAXUS = 2
    MAPLE = 3
    RED_MAPLE = 4
    WHITE_PINE = 5
    BLACK_PINE = 6

class TreeStyles(Enum):
    BROOM = 1
    FORMAL_UPRIGHT = 2
    INFORMAL_UPRIGHT = 3
    SLANTING = 4
    CASCADE = 5
    SEMI_CASCADE = 6
    LITERATI = 7
    MULTIPLE_TRUNK = 8
    FOREST = 9

class TreeParts(Enum):
    VASE = 1
    TRUNK = 2
    DEADWOOD = 3
    LEAVES = 4
    FLOWERS = 5