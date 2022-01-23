from trunk import Trunk
from vase import *
from pyvox.models import Vox
from pyvox.writer import VoxWriter

class Tree:

    def __init__(self, size, species, style):
        print(size, species, style)
        self.size = size
        self.species = species
        self.style = style

        self.treeMatrix = self.generateEmptyMatrix()
        self.generateVase()
        self.generateTrunk()
        self.generateDeadwood()
        self.generateLeaves()
        self.generateFlowers()

    def generateEmptyMatrix(self):
        s = treeSizes[self.size].width
        matrix = np.zeros((s,s,s*2), dtype=int)
        return matrix

    def generateVase(self):
        i = TreeParts.VASE.value
        #self.treeMatrix = getCompatibleVases(self.size, self.species, self.style)[0]
        #self.treeMatrix = getDefaultVase(self)

    def generateTrunk(self):
        trunkMatrix = Trunk(self.size, self.species, self.style).trunkMatrix
        self.treeMatrix = trunkMatrix #numpy.concatenate((self.treeMatrix, trunkMatrix))

    def generateDeadwood(self):
        i = TreeParts.DEADWOOD.value

    def generateLeaves(self):
        i = TreeParts.LEAVES.value

    def generateFlowers(self):
        i = TreeParts.FLOWERS.value

    def generateVOX(self, fileName):
        vox = Vox.from_dense(np.flip(np.rot90(tree.treeMatrix)))
        VoxWriter(fileName, vox).write()



tree = Tree(TreeSizes.MAME, TreeSpecies.MAPLE, TreeStyles.FORMAL_UPRIGHT)
tree.generateVOX('test.vox')