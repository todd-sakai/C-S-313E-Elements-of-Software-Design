def selection_sort(my_list):
    """
        Purpose:
            1. Sorts a list using selection sort.
        Input:
            [my_list]: A list of integers to be sorted.
        Variables:
            [comparisons]: Counts every time two elements are compared.
            [swaps]: Counts each time the selected number is swapped into its sorted position.
        Output:
            [comparisons, swaps]: A tuple containing the total performance counts.
    """
    comparisons = 0
    swaps = 0
    for i in range(len(my_list) - 1):
        index = i
        for j in range(i + 1, len(my_list)):
            comparisons += 1
            if my_list[j] < my_list[index]:
                index = j
        my_list[i], my_list[index] = my_list[index], my_list[i]
        swaps += 1
    return comparisons, swaps
#####################################################################################################################
def insertion_sort(my_list):
    """
        Purpose:
            1. Sorts a list using insertion sort.
        Input:
            [my_list]: A list of integers to be sorted.
        Variables:
            [comparisons]: Counts each check made to find the insertion point.
            [swaps]: Counts each time an element is shifted/swapped to make room.
        Output:
            [comparisons, swaps]: A tuple containing the total performance counts.
    """
    comparisons = 0
    swaps = 0
    for i in range(1, len(my_list)):
        j = i
        while True:
            if j <= 0:
                break
            comparisons += 1
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                swaps += 1
                j -= 1
            else:
                break
    return comparisons, swaps
#####################################################################################################################
def partition(my_list, i, k):
    """
        Purpose:
            1. Organizes a sub-section of a list around a pivot element so that all elements smaller than the pivot
               are to its left and all  elements larger are to its right.
        Input:
            [my_list]: The list of integers being sorted.
            [i]: The starting index of the sub-section to partition.
            [k]: The ending index of the sub-section to partition.
        Variables:
            [pivot]: The middle element
            [comparisons]: Counts the number of times elements are compared to the pivot.
            [swaps]: Counts the number of times elements are swapped to the correct side of the pivot.
        Output:
            [high, comparisons, swaps]: A tuple containing the split-point index and the performance counts.
    """
    comparisons = 0
    swaps = 0
    pivot = my_list[(i + k) // 2]
    done = False
    low = i
    high = k
    while not done:
        while my_list[low] < pivot:
            comparisons += 1
            low = low + 1
        comparisons += 1

        while my_list[high] > pivot:
            comparisons += 1
            high = high - 1
        comparisons += 1

        if low >= high:
            done = True
        else:
            my_list[low], my_list[high] = my_list[high], my_list[low]
            low = low + 1
            high = high - 1
            swaps += 1
    return high, comparisons, swaps
#####################################################################################################################
def _quick_sort(my_list, i, k):
    """
        Purpose:
            1. Sorts a list using quick sort.
        Input:
            [my_list]: A list of integers to be sorted.
        Variables:
            [comparisons]: Counts the comparisons made against the pivot during partitioning.
            [swaps]: Counts the swaps made to organize elements around the pivot.
        Output:
            [comparisons, swaps]: A tuple containing the total performance counts.
    """
    if i >= k:
        return 0, 0

    j, partition_comparisons, partition_swaps = partition(my_list, i, k)

    left_comparisons, left_swaps = _quick_sort(my_list, i, j)
    right_comparisons, right_swaps = _quick_sort(my_list, j + 1, k)
    total_comparisons = partition_comparisons + left_comparisons + right_comparisons
    total_swaps = partition_swaps + left_swaps + right_swaps
    return total_comparisons, total_swaps
#####################################################################################################################
def quick_sort(my_list):
    comparisons, swaps = _quick_sort(my_list, 0, len(my_list) - 1)
    return comparisons, swaps
