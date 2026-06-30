import sys
######################################################################################################################
class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None
######################################################################################################################
class Tree:
    def __init__(self, key):
        self.root = None
        for char in key:
            self.insert(char)

    def insert(self, ch):
        if self.root == None:
            self.root = Node(ch)
        else:
            self.insert_helper(self.root, ch)

    def insert_helper(self, node, ch):
        if ch < node.ch:
            if node.left == None:
                node.left = Node(ch)
            else:
                self.insert_helper(node.left, ch)
        elif ch > node.ch:
            if node.right == None:
                node.right = Node(ch)
            else:
                self.insert_helper(node.right, ch)

    def BST_print(self):
        if self.root == None:
            return
        self.BST_print_helper(self.root)

    def BST_print_helper(self, node, level=0):
        if node != None:
            if node.right != None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left != None:
                self.BST_print_helper(node.left, level + 1)

    def encrypt(self, message):
        """
        Purpose:
            1. Encrypts the input message using the cipher key stored in the BST
        Input:
            [message]: The input message that will be encrypted
        Variables:
            [encrypted_chars]: A list storing the BST paths for each character
            [ch]: The current character being processed
            [curr]: The current node being traversed
            [path]: A string bieng built that represents the path to the node
            [found]: A boolean that represents if the character was found in the BST
        Output:
            [str]: The final encrypter message
        """
        encrypted_chars = []
        for ch in message:
            if self.root == None:
                continue

            if ch == self.root.ch:
                encrypted_chars.append("*")
                continue
                
            curr = self.root
            path = ""
            found = False
            
            while curr != None:
                if ch == curr.ch:
                    found = True
                    break
                elif ch < curr.ch:
                    path += "<"
                    curr = curr.left
                else:
                    path += ">"
                    curr = curr.right
                    
            if found:
                encrypted_chars.append(path)
  
        return "!".join(encrypted_chars)

    def decrypt(self, codes_string):
        """
        Purpose:
            1. Decrypts the input string using the cipher key stored in the BST
        Input:
            [codes_string]: The encrypted string with paths separated by '!'
        Variables:
            [decrypted_message]: The final translated message being build
            [codes]: A list of individual character paths split from the input string
            [curr]: Represents the current node being traversed
            [code]: The specific path being translated
            [symbol]: The directional symbol ('<', '>') dictating the traversal direction
        Output:
            [str]: The decrypted, orignal message
        """
        if not codes_string:
            return ""
            
        decrypted_message = ""
        codes = codes_string.split("!")
        
        for code in codes:
            if not code:
                continue
                
            curr = self.root
            
            if code == "*":
                if curr != None:
                    decrypted_message += curr.ch
            else:
                for symbol in code:
                    if curr == None:
                        break
                    if symbol == "<":
                        curr = curr.left
                    elif symbol == ">":
                        curr = curr.right
                
                if curr != None:
                    decrypted_message += curr.ch
                    
        return decrypted_message
######################################################################################################################
''' DRIVER CODE '''
if __name__ == "__main__":
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()
    print(key_tree.encrypt(text_message))

    # read string to be decrypted
    coded_message = in_data.readline().strip()
    print(key_tree.decrypt(coded_message))
