import sys
######################################################################################################################
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False
        self.frequency = 0 # Tracks how many times this word was searched
######################################################################################################################
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word_end = True
        current.frequency += 1
    
    # A helper method to add a list of words that
    # were previously searched to the Trie
    # Input: history - a file handle where the first line
    #                  is the number of words to be added
    def add_history(self, history):
        num_words = int(history.readline())
        for i in range(num_words):
            self.insert(history.readline().rstrip())
    
    # A helper method to read each prefix to autocomplete
    # and prints the list of results
    # Input: requests - a file handle where the first line
    #                   is the number of prefixes to request
    def process_requests(self, requests):    
        num_requests = int(requests.readline())
        for i in range(num_requests):
            request = requests.readline().rstrip()
            print("Looking for: " + request)
            print("Got: " + str(trie.autocomplete(request)))
            print()
        
    def find_words(self, node, prefix, results):
        """
        Purpose:
            1. Walk the Trie from a given node and collect every complete word found
        Input:
            [node]: The TrieNode we're currently visiting
            [prefix]: The string built up along the path to this node
            [results]: The list we're appending (word, frequency) tuples to
        Variables:
            [char]: A character key in the node's children
            [child_node]: The TrieNode that character points to
        Output:
            [None]: Builds up results in place, nothing returned
        """
        if node.is_word_end:
            results.append((prefix, node.frequency))
            
        for char, child_node in node.children.items():
            self.find_words(child_node, prefix + char, results)
    
    def autocomplete(self, prefix):
        """
        Purpose:
            1. Collect all words in the Trie that begin with the given prefix
            2. Sort them by frequency, highest first
        Input:
            [prefix]: The prefix string to search for
        Variables:
            [current]: The node we're currently sitting at during traversal
            [results]: The list accumulating (word, frequency) tuples
            [n]: Length of results, used as the sort bound
            [i]: Outer loop index for sort
            [j]: Inner loop index for srt
        Output:
            [list]: Words matching the prefix, sorted most to least frequent
        """
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
            
        results = []
        self.find_words(current, prefix, results)
        
        n = len(results)
        for i in range(n):
            for j in range(0, n - i - 1):
                if results[j][1] < results[j + 1][1]:
                    results[j], results[j + 1] = results[j + 1], results[j]
        
        return [word for word, frequency in results]
######################################################################################################################
''' DRIVER CODE '''
if __name__ == "__main__":
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('autocomplete.in')
    else:
        in_data = sys.stdin

    # Setup the Trie for future autocomplete requests
    trie = Trie()
    trie.add_history(in_data)

    # Process requests
    trie.process_requests(in_data)
