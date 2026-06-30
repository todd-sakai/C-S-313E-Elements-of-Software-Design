from TreeCompareNode import TreeCompareNode

class TreeCompare:
    # Make sure to add the AVL boolean as an input
    def __init__(self, AVL):
        self.root = None
        self.AVL = AVL
    
    def _inorder_traversal(self, current):
        if current is not None:
            self._inorder_traversal(current.left)
            print(current)
            self._inorder_traversal(current.right)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def insert(self, key):
        new_node = TreeCompareNode(key)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node is not None:
                if new_node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = new_node
                        new_node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        new_node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.right

            current_node = new_node.parent

            if self.AVL == True:
                while current_node is not None:
                    self.rebalance(current_node)
                    current_node = current_node.parent

    def rotate_left(self, node):
        right_left_child = node.right.left

        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None

        node.right.set_child('left', node)
        node.set_child('right', right_left_child)

        return node.parent

    def rotate_right(self, node):
        left_right_child = node.left.right

        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None

        node.left.set_child('right', node)
        node.set_child('left', left_right_child)

        return node.parent

    def rebalance(self, node):
        node.update_height()

        if node.get_balance() == -2:
            if node.right.get_balance() == 1:
                self.rotate_right(node.right)
            return self.rotate_left(node)
        elif node.get_balance() == 2:
            if node.left.get_balance() == -1:
                self.rotate_left(node.left)
            return self.rotate_right(node)
        return node
    
    def height_HELPER(self, node):
            """
            Purpose:
                1. Recursively compute the height of the subtree rooted at node
            Input:
                [node]: The node to measure from, None represents an empty subtree
            Variables:
                None
            Output:
                [int]: Height of the subtree (-1 if node is None, 0 for a single leaf)
            """
            if node == None:
                return -1
            else:
                return 1 + max(self.height_HELPER(node.left), self.height_HELPER(node.right))
            
    def height(self): 
        """
        Purpose:
            1. Return the height of the entire tree
        Input:
            None
        Variables:
            None
        Output:
            [int]: Height of the tree, measured from the root to the deepest leaf
        """         
        return self.height_HELPER(self.root)
    
    def range(self):
        """
        Purpose:
            1. Compute the difference between the largest and smallest keys in the tree
        Input:
            None
        Variables:
            [minimum]: Node reference traversed left until the smallest key is found
            [maximum]: Node reference traversed right until the largest key is found
        Output:
            [int]: The max key minus the min key
        """
        minimum = self.root

        while minimum.left != None:
            minimum = minimum.left

        maximum = self.root

        while maximum.right != None:
            maximum = maximum.right

        return maximum.key - minimum.key
    
    def nodes_at_level_HELPER(self, node, current_level, target_level, output_nodes):
        """
        Purpose:
            1. Recursively collect the keys of all nodes at target_level
        Input:
            [node]: The node currently being visited
            [current_level]: The depth of node in the tree (root is 0)
            [target_level]: The depth whose node keys we want to collect
            [output_nodes]: List that matching keys are appended to in place
        Variables:
            None
        Output:
            [None]: Results are written directly into output_nodes
        """
        if node == None:
            return
        elif current_level == target_level:
            output_nodes.append(node.key)
            return
        else:
            self.nodes_at_level_HELPER(node.left, current_level + 1, target_level, output_nodes)
            self.nodes_at_level_HELPER(node.right, current_level + 1, target_level, output_nodes)

    def nodes_at_level(self, level):
        """
        Purpose:
            1. Return a list of all keys at the given depth level
        Input:
            [level]: The target depth to collect keys from (root is level 0)
        Variables:
            [output_nodes]: Accumulator list passed into nodes_at_level_HELPER
        Output:
            [list]: Keys of every node at that level, ordered left to right
        """
        output_nodes = []
        self.nodes_at_level_HELPER(self.root, 0, level, output_nodes)
        return output_nodes
    
    def sum_leaves_HELPER(self, node):
        """
        Purpose:
            1. Recursively sum the keys of all leaf nodes in the subtree rooted at node
        Input:
            [node]: The node currently being visited
        Variables:
            None
        Output:
            [int]: Sum of all leaf keys in this subtree (0 if node is None)
        """
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return node.key
        else:
            return self.sum_leaves_HELPER(node.left) + self.sum_leaves_HELPER(node.right)

    def sum_leaves(self):
        """
        Purpose:
            1. Return the sum of all leaf node keys in the tree
        Input:
            None
        Variables:
            None
        Output:
            [int]: Total of all leaf keys
        """
        return self.sum_leaves_HELPER(self.root)

    def left_view(self):
        """
        Purpose:
            1. Return the left-side view of the tree (the first visible node at each level)
        Input:
            None
        Variables:
            [level_nodes]: Dictionary mapping each depth level to its list of node keys
            [left_leaves]: Accumulator list for the leftmost key at each level
        Output:
            [list]: Keys of the leftmost node at each level, from root to bottom
        """
        level_nodes = {}
        left_leaves = []

        for level in range(self.height() + 1):
            level_nodes[level] = self.nodes_at_level(level)

        for level in level_nodes:
            left_leaves.append(level_nodes[level][0]) 
        
        return left_leaves

    def print(self):
        self.print_helper(self.root)

    def print_helper(self, current, level=0):
        if current.right is not None:
            self.print_helper(current.right, level + 1)

        print(' ' * 3 * level + '->', current.key)

        if current.left is not None:
            self.print_helper(current.left, level + 1)
