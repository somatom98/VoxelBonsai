from examples.treeConstants import TreeSizes


class TreeSize():
    def __init__(self, name, width, depth, minHeight, maxHeight):
        self.name = name
        self.width = width
        self.depth = depth
        self.minHeight = minHeight
        self.maxHeight = maxHeight

treeSizes = {
    TreeSizes.MAME: TreeSize("Mame", 5, 5, 5, 10),
    TreeSizes.SHOHIN: TreeSize("Shohin", 9, 9, 9, 18),
    TreeSizes.CHUHIN: TreeSize("Chuhin", 15, 15, 15, 30),
    TreeSizes.DAI: TreeSize("Dai", 23, 23, 23, 46),
}