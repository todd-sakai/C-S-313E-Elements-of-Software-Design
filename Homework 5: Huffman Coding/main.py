import sys
from HuffmanTree import *

def main():
    """
    Purpose:
        1. Generates and prints the Huffman Tree based on the set key
        2. Reads all input lines from input
        3. Compresses and decompresses each valid line
    Input:
        None
    Variables:
        [MESSAGE_KEY]: The message key
        [huff_tree]: A HuffmanTree object generated from the MESSAGE_KEY
        [lines]: A list of strings representing the lines from the input data
        [line]: A string representing the current line being looked at
        [original_message]: A string of the cleaned-up line
        [compressed_message]: A string of binary digits returned by the compress method
        [decompressed_message]: A decoded string returned by the decompress method
    Output:
        None: Prints out resulting characters and their binary code along with the original
    """
    MESSAGE_KEY = "when zombies arrive, quickly fax judge pat.9876543210"
    
    huff_tree = HuffmanTree(MESSAGE_KEY)
    print(huff_tree)

    lines = sys.stdin.readlines()
    
    for line in lines:
        original_message = line.strip('\r\n')
        
        if original_message == "":
            continue
            
        compressed_message = huff_tree.compress(original_message)
        decompressed_message = huff_tree.decompress(compressed_message)
        
        print(f"Original: {original_message}")
        print(f"Compressed: {compressed_message}")
        print(f"Decompressed: {decompressed_message}")

''' You WILL need to update __main()__ for this assignment '''
if __name__ == "__main__":
    main()
