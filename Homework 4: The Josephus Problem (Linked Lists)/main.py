import sys
#####################################################################################################################
class Link(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
#####################################################################################################################
class CircularList(object):
    def __init__(self):
        self.first = None
        self.last = None


    def is_empty(self):
        return self.first is None


    def insert(self, data):
        """
        Purpose:
            1. Creates a new node with the input data and appends it to the end of the circular list
        Input:
            [data]: The value to be stored in the new node
        Variables:
            [new_node]: The new node created
        Output:
            [None]: This is a class method 
        """
        new_node = Link(data)
        if self.is_empty() == True:
            self.first = new_node
            self.last = new_node
            self.last.next = self.first
        else:
            self.last.next = new_node
            self.last = new_node
            self.last.next = self.first
        pass


    def find(self, data):
        """
        Purpose:
            1. Searches the circular list to find and return the node containing the input data
        Input:
            [x]: The value to be searched for in the circular list
        Variables:
            [current]: The current node being searched
        Output:
            [None]: No node containing the input data exists in the circular list
            [current]: The node containng the input data
        """
        if self.is_empty() == True:
            return None
        
        current = self.first
        while True:
            if current.data == data:
                return current
            current = current.next
            
            if current == self.first:
                break
        return None
        pass


    def delete(self, data):
        """
        Purpose:
            1. Removes the node with the input data from the circular list and return it
        Input:
            [data]: The value to search for within the circular list
        Variables:
            [current]: The current node being searched
        Output:
            [None]: No node containing the input data exists in the circular list
            [current]: The node containng the input data
        """
        if self.is_empty() == True:
            return None
        
        current = self.first
        previous = self.last

        while True:
            if current.data == data:
                if current == self.first:
                    if self.first == self.last:
                        self.first = None
                        self.last = None
                    else:
                        self.first = self.first.next
                        self.last.next = self.first
                else:
                    previous.next = current.next
                    if current == self.last:
                        self.last = previous
                return current
            
            previous = current
            current = current.next

            if current == self.first:
                break
        return None
        pass


    def delete_after(self, start, step):
        """
        Purpose:
            1. Removes the node that is a certain number of steps away after the starting node
        Input:
            [start]: The node from which the counting begins
            [step]: The number of nodes to traverse before removing a node
        Variables:
            [current]: The current node being iterated through
            [to_delete]: The node to be deleted
            [next_start]: The node directly after the removed node
        Output:
            [to_delete.data, next_start]: The data of the removed node and the node folliwng it
        """
        current = start
        for i in range(step - 1):
            current = current.next
        
        to_delete = current
        next_start = to_delete.next
         
        self.delete(to_delete.data)

        return to_delete.data, next_start
        pass


    def __str__(self):
        """
        Purpose:
            1. Returns a string of the circular list
        Input:
            [None]: None
        Variables:
            [output_str]: The string of the circular list
            [current]: The current node being added to the string
        Output:
            [output_str]: The final string of the circularl list
        """
        if self.is_empty == True:
            return "[]"
        
        output_str = "["
        current = self.first
        while True:
            output_str += str(current.data)
            current = current.next
            if current == self.first:
                break
            output_str += ", "
        output_str += "]"
        pass
#####################################################################################################################
def create_circular_list(num_participants):
    """
    Purpose:
        1. creates a circular list with nodes numbered 1 to the given number of participants
    Input:
        [num_participants]: The number of nodes in the list
    Variables:
        [output_list]: The circular list being created
        [i]: Loop variable
    Output:
        [output_list]: The final circular list
    """
    output_list = CircularList()

    for i in range (1, num_participants + 1):
        output_list.insert(i)
    return output_list
    pass
#####################################################################################################################
def process_Josephus(my_list, num_participants, start_data, step_count):
    """
    Purpose:
        1. Follows the Josephus algorithm, starting at a specific participant and continually removing participants
           based on the step count until none remain
    Input:
        [my_list]: The populated circular list of participants
        [num_participants]: The total number of participants in the list
        [start_data]: The value of the participant to start counting from
        [step_count]: The number of people to count before removing a participant
    Variables:
        [current]: The node from which the current round of counting begins
        [removed_data]: The data of the participant that was just removed
    Output:
        [None]: The method prints the order of removed participants to the console
    """
    if my_list.is_empty() == True:
        return
    
    current = my_list.find(start_data)

    while my_list.is_empty() == False:
        removed_data, current = my_list.delete_after(current, step_count)
        print(removed_data)
    pass
#####################################################################################################################
''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''
if __name__ == "__main__":
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
    else:
        in_data = sys.stdin
    data = in_data.read()
    data_list = data.split('\n')
    num_participants = int(data_list[0])
    start = int(data_list[1])
    step = int(data_list[2])

    # Create cirular list
    my_list = create_circular_list(num_participants)

    # Remove participants
    process_Josephus(my_list, num_participants, start, step)
