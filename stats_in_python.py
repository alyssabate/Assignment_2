import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    pass

def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    total = sum(numbers)
    count = len(numbers)
    return total/count

def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    if len(numbers) == 1:
        return 0.0
    average = calculate_average(numbers)
    total = 0
    for x in numbers:
        diff = (x - average) **2
        total = total + diff
    return total /(len(numbers)-1)

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_list = sorted(number)
    middle = len(sorted_list)// 2
    if len(sorted_list) % 2 == 1:
        return float(sorted_list[middle])
    else:
        return (sorted_list[middle -1] + sorted_list[middle])/2




