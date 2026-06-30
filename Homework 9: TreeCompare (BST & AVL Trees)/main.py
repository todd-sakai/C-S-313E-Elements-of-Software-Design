import sys
from TreeCompare import TreeCompare

if __name__ == "__main__":
# Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open("tree.in")
    else:
        in_data = sys.stdin

    # Read values to add to tree
    line = in_data.readline().strip()
    line = line.split()
    tree_input = list(map(int, line))  # converts elements into ints

    # Read tree level to print
    level = int(in_data.readline().strip())

    # Create and print tree info for AVL Tree
    AVLtree = TreeCompare(True)

    for value in tree_input:
        AVLtree.insert(value)

    print("===== AVL TREE =====")
    # Use this line for debugging, make sure to remove before submitting
    # AVLtree.print()
    print("Tree height:", AVLtree.height())
    print("Tree range:", AVLtree.range())
    print("Values at level ", level, " :", AVLtree.nodes_at_level(level))
    print("Sum of leaf nodes:", AVLtree.sum_leaves())
    print("Tree left side view:", AVLtree.left_view())
    print()

    # Create and print tree info for AVL Tree
    BSTree = TreeCompare(False)
    for value in tree_input:
        BSTree.insert(value)

    print("======== BST =======")
    # Use this line for debugging, make sure to remove before submitting
    # BSTree.print()
    print("Tree height:", BSTree.height())
    print("Tree range:", BSTree.range())
    print("Values at level ", level, " :", BSTree.nodes_at_level(level))
    print("Sum of leaf nodes:", BSTree.sum_leaves())
    print("Tree left side view:", BSTree.left_view())
