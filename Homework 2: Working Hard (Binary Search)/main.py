import sys
import time
#####################################################################################################################
def sum_series(lines_before_coffee, prod_loss, lines_written, num_coffees):
    pass
    """
    Purpose:
        1. Recursively calculate the total number of lines of code written
           by simulating productivity loss until the number of new lines
           written reaches zero.
    Input:
        [lines_before_coffee]: The starting number of lines to be divided in
                               the current recursive step.
        [prod_loss]: The current divisor used to calculate productivity loss
                     (doubles with every recursive call in this implementation).
        [lines_written]: The running total of lines of code accumulated so far.
        [num_coffees]: The counter for the depth of recuson (number of
                       coffees consumed).
    Variables:
        [new_lines]: The number result of dividing the current lines by
                     the productivity loss.
        [recursive_calls]: The final count of function calls returned when
                           the base case is reached.
    Output:
        [lines_written]: The total number of lines of code Chris can write
                         given the inputs.
        [recursive_calls]: The total number of times this function was called.
    """
    new_lines = lines_before_coffee // prod_loss
    
    if new_lines == 0:
        recursive_calls = num_coffees + 1
        return lines_written, recursive_calls
    else:
        return sum_series(new_lines, prod_loss, lines_written + new_lines, num_coffees + 1)
#####################################################################################################################
def linear_search(total_lines, prod_loss):
    pass
    """
    Purpose:
        1. Find the minimum initial lines of code required to meet the target
           by checking every number linearlly from 0 up to total_lines.
    Input:
        [total_lines]: The goal number of lines of code Chris needs to write.
        [prod_loss]: The initial productivity loss factor.
    Variables:
        [possible_lines_before_coffee]: A list containing every number from
                                        0 to total_lines - 1.
        [num_sum_series]: A tuple containing the (lines_written, recursive_calls)
                          returned by sum_series for the current number.
    Output:
        [num]: The first (smallest) number found that results in enough
               lines written to meet the target.
        [recursive_calls]: The total number of times sum_series was called
                           during the search.
    """
    recursive_calls = 0
    
    for num in range(total_lines + 1):
        num_sum_series = sum_series(num, prod_loss, num, 0)
        lines_written = num_sum_series[0]
        recursive_calls += num_sum_series[1]
        
        if lines_written < total_lines:
            continue
        else:
            return num, recursive_calls
#####################################################################################################################
def binary_search(total_lines, prod_loss):
    pass
    """
    Purpose:
        1. Find the minimum initial lines of code required to meet the target
           using a binary search algorithm to minimize checks.
    Input:
        [total_lines]: The goal number of lines of code Chris needs to write.
        [prod_loss]: The initial productivity loss factor.
    Variables:
        [leftmost]: The lower bound index of the search space.
        [rightmost]: The upper bound index of the search space.
        [mid]: The midpoint value being tested in the current iteration.
        [lines_before_coffee]: Stores the smallest valid answer found so far.
        [mid_sum_series]: A tuple containing the (lines_written, recursive_calls)
                          returned by sum_series for the 'mid' value.
    Output:
        [lines_before_coffee]: The smallest initial value found that allows
                               Chris to complete the total_lines.
        [recursive_calls]: The total number of times sum_series was called
                           during the search.
    """
    leftmost = 0
    rightmost = total_lines
    recursive_calls = 0
    lines_before_coffee = -1
    
    while rightmost >= leftmost:
        mid = (rightmost + leftmost) // 2
        mid_sum_series = sum_series(mid, prod_loss, mid, 0)
        lines_written = mid_sum_series[0]
        recursive_calls += mid_sum_series[1]
        
        if lines_written >= total_lines:
            lines_before_coffee = mid
            rightmost = mid - 1
        else:
            leftmost = mid + 1
    return lines_before_coffee, recursive_calls
#####################################################################################################################
def process_data(data):
    num_cases = int(data[0].strip())
    # Loop once per case
    for i in range(num_cases):

        # read one line for one case
        line = data[i + 1].strip().split()
        total_lines = int(line[0])  # total number of lines of code
        prod_loss = int(line[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time), "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time), "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()
#####################################################################################################################
''' ##### DRIVER CODE ##### '''

if __name__ == "__main__":
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin
    data = in_data.readlines()
    process_data(data)
