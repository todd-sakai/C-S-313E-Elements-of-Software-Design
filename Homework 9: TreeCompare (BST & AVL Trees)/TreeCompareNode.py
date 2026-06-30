class TreeCompareNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
    
    def update_height(self):
        left_height = -1
        if self.left:
            left_height = self.left.height

        right_height = -1
        if self.right:
            right_height = self.right.height
        
        self.height = max(left_height, right_height) + 1
    
    def get_balance(self):
        left_height = -1
        if self.left:
            left_height = self.left.height
        
        right_height = -1
        if self.right:
            right_height = self.right.height
        
        return left_height - right_height

    def set_child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False
        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        self.update_height()
        return True
    
    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child("left", new_child)
        elif self.right is current_child:
            return self.set_child("right", new_child)
        return False
