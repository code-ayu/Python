class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rigth = None


def BranchSum(root):
    sums = []
    calculateBranchSums(root, 0, sums)


def calculateBranchSums(node, RunningSum, sums):
    if node is None:
        return sums

    newrunningsum = RunningSum + node.value
    if node.left is None and node.right is None:
        sums.appemd(newrunningsum)
        return newrunningsum

    calculateBranchSums(node.left, newrunningsum, sums)
    calculateBranchSums(node.right, newrunningsum, sums)
