import sys
from Stack import *

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']

# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)

class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__(self):
        self.root = Node(None)

    def create_tree(self, expr):
        """
        Purpose:
            1. Modifies/builds a binary search tree turning each characted from the provided mathematical expression into a node
        Input:
            [expr]: The mathematical expression to be turned into a BST
        Variables:
            [chars]: A list of the characters from the input expression
            [stack]: A Stack object used to keep track of parent nodes while navigating down the BST
            [current]: A Node object tracking the current node in the tree
        Output:
            Nothing, this method just modifies/builds the BST in place
        """
        chars = expr.split()
        stack = Stack()
        current = self.root

        for char in chars:
            if char == "(":
                current.lChild = Node(None)
                stack.push(current)
                current = current.lChild
            elif char in operators:
                current.data = char
                stack.push(current)
                current.rChild = Node(None)
                current = current.rChild
            elif char == ")":
                if stack.is_empty() == False:
                    current = stack.pop()
            else:
                current.data = char
                current = stack.pop()

    def evaluate(self, current):
        """
        Purpose:
            1. Recursively calls itself, navigating the expression tree to calculate the given mathematical expression
        Input:
            [current]: The current node being looked at
        Variables:
            [left_val]: The calculated mathematical result of the left subtree
            [right_val]: The calculated mathematical result of the right subtree
        Output:
            The calculated value of the current sub-expression or the final expression
        """
        if current.lChild == None and current.rChild == None:
            return int(current.data)
        else:
            left_val = self.evaluate(current.lChild)
            right_val = self.evaluate(current.rChild)
        return operation(current.data, left_val, right_val)


    def pre_order(self, current):
        """
        Purpose:
            1. Generates the prefix notation of the expression using a Root-Left-Right tree traversal
        Input:
            [current]: The current node being looked at
        Variables:
            [result]: The prefix order formatted expression
        Output:
            [result]: The final input expression formatted in prefix order
        """
        if current == None:
            result = ""
        else:
            result = str(current.data) + " "
            result += self.pre_order(current.lChild)
            result += self.pre_order(current.rChild)
        return result


    def post_order(self, current):
        """
        Purpose:
            1. Generates the post fix notation of the expression using a Left-Right-Rood tree traversal
        Input:
            [current]: The current node being looked at
        Variables:
            [result]: The post fix order formatted expression
        Output:
            [result]: The final input expression formatted in post fix order
        """
        if current == None:
            return ""
        else:
            result = ""
            result += self.post_order(current.lChild)
            result += self.post_order(current.rChild)
            result += str(current.data) + " "
        return result
