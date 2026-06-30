import sys
from PriorityQueue import PriorityQueue

class HuffmanNode(object):
    def __init__(self, ch=None, count=0, left=None, right=None):
        self.ch = ch
        self.count = count
        self.left = left
        self.right = right
        self.code = ''

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        result = []
        if self.ch:
            result.append(f'{self.ch} {self.count} - Code: {self.code}')
        if self.left:
            result.append(self.left.__str__())
        if self.right:
            result.append(self.right.__str__())
        return '\n'.join(result)

class HuffmanTree():
    def __init__(self, input=''):
        self.freq_table = {}
        self.build_freq_table(input)
        self.root = self.build_tree(input)
        self.generate_codes(self.root, '')

    def __str__(self):
        if self.root is None:
            return ''
        else:
            return str(self.root)

    def build_freq_table(self, inputString):
        for i in range(len(inputString)):
            key = inputString[i]
            if key in self.freq_table.keys():
                self.freq_table[key] = self.freq_table[key] + 1
            else:
                self.freq_table[key] = 1

    def build_tree(self, inputString):
        # Build a priority queue of frequency, character pairs
        priorities = PriorityQueue()
        for key in self.freq_table:
            node = HuffmanNode(ch=key, count=self.freq_table[key])
            priorities.push(node)

        # Builds a huffman tree
        while (priorities.get_size() > 1):
            # Dequeue 2 lowest-priority nodes
            left = priorities.pop()
            right = priorities.pop()

            # Make a parent for the two nodes
            freqSum = right.count + left.count
            parent = HuffmanNode(count=freqSum, left=left, right=right)

            # Enqueue parent back into priority queue
            priorities.push(parent)

        # Return root of the huffman tree
        return priorities.pop()

    def generate_codes(self, node, code):
        if node is None:
            return
        node.code = code
        self.generate_codes(node.left, code + '0')
        self.generate_codes(node.right, code + '1')

    def get_code_dict(self):
        """
        Purpose:
            1. Initializes an empty dictionary to store characters and their binary codes
            2. Calls a helper function to fill this dictionary by going through the tree
        Input:
            None
        Variables:
            [my_dict]: A dictionary that will map each character to its corresponding binary code string
        Output:
            [my_dict]: A filled dictionary containing character to code mappings
        """
        my_dict = {}
        self.helper(self.root, my_dict)
        return my_dict

    def helper(self, node, my_dict):
        """
        Purpose:
            1. Looks throguh the Huffman tree to find leaf nodes
            2. When a leaf node that contains a character is found, the character and its binary code is added to the dictionary
        Input:
            [node]: A HuffmanNode representing the current position in the tree
            [my_dict]: A dictionary that store the characters and their codes
        Variables:
            None
        Output:
            None
        """
        if node == None:
            return
        
        if node.ch != None:
            my_dict[node.ch] = node.code
            
        self.helper(node.left, my_dict)
        self.helper(node.right, my_dict)

    def compress(self, text):
        """
        Purpose:
            1. Converts the input text to lowercase
            2. Gets the dictionary of Huffman codes
            3. Loops through each character in the text and appends its code to a result string
        Input:
            [text]: A string containing the message to be compressed
        Variables:
            [codes]: A dictionary containing the character-to-code mappings from the tree
            [result]: A string representing the final compressed message
            [char]: A string representing the current character being iterated through in the text
        Output:
            [result]: A string of 1s and 0s representing the compressed text
        """
        text = text.lower()
        codes = self.get_code_dict()
        result = ""
        
        for char in text:
            if char in codes:
                result += codes[char]
                
        return result

    def decompress(self, code):
        """
        Purpose:
            1. Reads a string of binary digits one by one
            2. Traverses left for 0 and right for 1 down the Huffman tree
            3. When a leaf node with a character is reached, it is added to the result and restarts from the root
        Input:
            [code]: A string of 1s and 0s representing the compressed message
        Variables:
            [result]: A string building the final decoded text message
            [current_node]: A HuffmanNode representing the current position in the tree traversal
            [bit]: A string representing the current 1s and 0s being evaluated
        Output:
            [string]: The decompressed original text message
        """
        result = ""
        current_node = self.root
        
        for bit in code:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right
                
            if current_node.ch is not None:
                result += current_node.ch
                current_node = self.root
                
        return result
