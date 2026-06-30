import sys

def get_dimension(in_data):
    pass
    """    
    Purpose:
        1. Validate and return the desired size for the number spiral
           as an integer.
    Input:
        [in_data]: This is the plain text file containg all the inputs
                   needed to generate the number spiral.
    Variables:
        [spiral_size]: This is the first line of the plain text file,
                       which is the desired size for the number spiral.
    Output:
        [-1]: This indicates the desired size of the number spiral was
              invalid. It either wasn't an integer or it wasn't a number
              1 through 99 (Inclusive).
        [n]: This indicates the desired size of the number spiral was valid.
        [n+1]: This indicates the desired size of the number spiral was valid,
               however n was even, so 1 must be added to ensure the number
               spiral has a center.
    """
    spiral_size = in_data.readline().strip()
    try:
        if spiral_size.isdigit() == False: # If the input provided isn't an integer then raise ValueError
            raise ValueError
        
        spiral_size = int(spiral_size) # If it get's here, then the provided number is an integer, so save it as an integer

        if spiral_size not in range(0,100): # If the input provided isn't between 0 and 99 then raise ValueError
            raise ValueError
        elif spiral_size % 2 == 0: # If the input is even then add 1 to make it odd
            return spiral_size + 1
        else:
            return spiral_size
    
    except ValueError: # Indicate the input provided isn't a valid size by printing a message and returning -1
        print("Invalid spiral size")
        return(-1)
#####################################################################################################################
def create_spiral(n):
    pass
    """    
    Purpose:
        1. Create a 2D  array of a number spiral with a size of n**2 (n squared).
    Input:
        [n]: This is the validated size provided from the get_dimension() function.
    Variables:
        [spiral]: This is the 2D array that will be storing the number spiral.
        [y]: This is the y-coordinate in the array, which is the row index.
        [x]: This is the x-coordinate in the array, which is the column index.
        [current_num]: This is the current number being added to the number spiral.
        [step]: This is how many blocks are walked in a straight line before turning.
    Output:
        [spiral]: This is the 2D array that is storing the number spiral. 
    """
    spiral = [[0 for num in range(n)] for num in range(n)] # This initializes the number spiral of size n**2 with 0s

    y = n//2 # This is the index of the middle row
    x = n//2 # This is the index of the middle column

    spiral[y][x] = 1 # This places 1 in the middle of the number spiral

    current_num = 2 # 2 is the current number to be added to the number spiral
    step = 1

    while current_num <= n**2: # Loop through the 2D array, filling it with numbers until it reaches n**2
        for num in range(step): # This moves the coordinates right (x + 1)
            if current_num > n**2:
                break
            x += 1
            spiral[y][x] = current_num
            current_num += 1
        
        for num in range(step): # This moves the coordinates down (y + 1)
            if current_num > n**2:
                break
            y += 1
            spiral[y][x] = current_num
            current_num += 1
        
        step += 1 # Turning, so increase the step (step + 1)

        for num in range(step): # This moves the coordinates left (x - 1)
            if current_num > n**2:
                break
            x -= 1
            spiral[y][x] = current_num
            current_num += 1
        
        for num in range(step): # This moves the coordinates up (y - 1)
            if current_num > n**2:
                break
            y -= 1
            spiral[y][x] = current_num
            current_num += 1

        step += 1 # Turning again, so increase step (step + 1)
    
    return spiral
#####################################################################################################################
def print_adjacent_sums(in_data, spiral):
    pass
    """    
    Purpose:
        1. Read numbers from in_data, calculate the sums of the numbers surrounding them,
           then print the sums.
    Input:
        [in_data]: This is a plain text file containing the numbers to calculate the adjacent
                   sums for.
        [spiral]: This is the number spiral provided, which will be referenced to caclulate the
                  adjacent sums.
    Variables:
        [line]: This represents the individual lines in in_data.
        [target_num]: This represents the number that the adjacent sum will be calculated for.
        [adj_sum]: This is the calculate adjacent sum of target_num.
    Output:
        [adj_sum]: Printed adjacent sums of all the valid numbers in in_data.
    """
    for line in in_data:
        try:
            target_num = line.strip()
            
            if target_num.isdigit() == False: # Check if target_num is an integer
                raise ValueError
            else:
                target_num = int(target_num)
                adj_sum = sum_adjacent_numbers(spiral, target_num)
                print(adj_sum)
        
        except ValueError: # If there's not an integer continue
            continue
#####################################################################################################################
def sum_adjacent_numbers(spiral, n):
    pass
    """    
    Purpose:
        1. Calculates the sum of all the numbers surrounding n in the number spiral.
    Input:
        [spiral]: This is the provided number spiral.
        [n]: This is the number that will be referenced when calculating the sum of
             its surrounding numbers.
    Variables:
        [size]: This is the height and width of the provided number spiral.
        [target_y]: This is the y-coordinate of the target number in the array, which
                    is the row index.
        [target_x]: This is the x-coordinate of the target number in the array, which
                    is the column index.
        [found]: This is a boolean that indicates if the targeted number was found or
                 not.
        [total_sum]: This is the sum of the numbers surrounding the targeted number.
        [offset_y]: This shifts the search row up or down.
        [offset_x]: This shifts the search column left or right.
        [neighbor_y]: This references the row coordinate of the neighbor being
                      checked.
        [neighbor_x]: This references the column coordinate of the neighbor being
                      checked.
    Output:
        [total_sum]: This is the calculated sum of the numbers surrounding the targeted
                     number.
    """
    size = len(spiral)
    target_y = -1
    target_x = -1

    found = False # Initialize found as false

    for x in range(size): # Find the coordinates of the targeted number n
        for y in range(size):
            if spiral[y][x] == n:
                target_y = y # Store the targeted y coordinate
                target_x = x # Store the targeted x coordinate
                found = True # Found so set found = to True
                break
        if found: # If n is found, exit the loop
            break
        
    if not found: # If n is not found in the number spiral, return 0
        return 0

    total_sum = 0 # Initialize the sum of the numbers surrounding n

    for offset_y in [-1,0,1]: # Check all numbers surrounding n
        for offset_x in [-1,0,1]:
            
            if offset_y == 0 and offset_x == 0: # Make sure to not add n
                continue

            neighbor_y = target_y + offset_y
            neighbor_x = target_x + offset_x

            if 0 <= neighbor_y < size and 0 <= neighbor_x < size: # Check if neighbor is in the number spiral
                total_sum += spiral[neighbor_y][neighbor_x]

    return total_sum
#####################################################################################################################
# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
# Input: spiral - the number spiral
# Output: printed spiral
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Remember to change the debug flag before submitting. '''
if __name__ == "__main__":
    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin
    
    # get the spiral size from the file
    size = get_dimension(in_data)
    
    # if valid spiral size
    if size != -1:
        
        # create the spiral
        spiral = [[]]
        spiral = create_spiral(size)
    
        # use following line for debugging only
        # print_spiral(spiral)
    
        # process and print adjacent sums
        print_adjacent_sums(in_data, spiral)


