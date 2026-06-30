from Sorts import *
import sys
import random
#####################################################################################################################
def run_test(sort_type, data):
    """
        Purpose:
            1. Performs a single test for a specific sorting algorithm.
        Input:
            [sort_type]: A string indicating which sorting algorithm to use.
            [data]: A list of integers representing the dataset to be sorted.
        Variables:
            [comparisons]: An integer tracking the number of comparisons made during the sort.
            [swaps]: An integer tracking the number of swaps made during the sort.
        Output:
            [comparisons, swaps]: A tuple containing the final count of comparisons and swaps.
    """
    comparisons = 0
    swaps = 0

    if sort_type == "selection":
        comparisons, swaps = selection_sort(data)
    elif sort_type == "insertion":
        comparisons, swaps = insertion_sort(data)
    elif sort_type == "quick":
        comparisons, swaps = quick_sort(data)
    else:
        comparisons, swaps = 0, 0

    return comparisons, swaps
#####################################################################################################################
def run_tests(sort_types, data_types, data_sets):
    results = {}
    for data in data_types:
        for sort in sort_types:
            data_copy = list(data_sets[data])
            results[(sort, data)] = run_test(sort, data_copy)
    return results
#####################################################################################################################
def read_data_sets(lines):
    data_sets = {}
    for i in range (len(lines) // 2):
        data_str_list = lines[i * 2 + 1].strip().split(', ')
        data_int_list = []
        for str in data_str_list:
            data_int_list.append(int(str))
        data_sets[lines[i * 2].strip()] = data_int_list
    return data_sets
#####################################################################################################################
def print_results(sort_types, data_sets, results):
    comparison_lines = {}
    swap_lines = {}
    for sort in sort_types:
        comparison_lines[sort] = ''
        swap_lines[sort] = ''
    heading1 = ' ' * 15
    heading2 = '(data size)'.ljust(15)
    for data_type, data_list in data_sets.items():
        heading1 += f"{data_type:>12}"
        data_size_str = '(' + str(len(data_list)) + ')'
        heading2 += f'{data_size_str:>12}'
    print(heading1)
    print(heading2)
    for (sort_type, data_type), (comparisons, swaps) in results.items():
        comparison_lines[sort_type] += f"{comparisons:12d}"
        swap_lines[sort_type] += f"{swaps:12d}"
    print('COMPARISONS')
    for sort, line in comparison_lines.items():
        print(f'{sort:15}{line}')
    print('SWAPS')
    for sort, line in swap_lines.items():
        print(f'{sort:15}{line}')
#####################################################################################################################
if __name__ == "__main__":
    sort_types = ['selection', 'insertion', 'quick']
    data_types = ['small', 'large', 'sorted', 'reversed']
    debug = False
    if debug:
        in_data = open('sort_data.in')
    else:
        in_data = sys.stdin
    lines = in_data.readlines()
    data_sets = read_data_sets(lines)
    results = run_tests(sort_types, data_types, data_sets)
    print_results(sort_types, data_sets, results)
