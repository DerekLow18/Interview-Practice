'''
This is mergeSort and bubbleSort in Python, just as a refresher
on the methods of performing these operations.
First, we do mergesort.

In merge sort, we have a list of numbers that we want to sort.
The sorting algorithm is divide and conquer, meaning that we
keep halving recursively until the lists can no longer be split,
then we merge the sorted sublists together.
'''

def mergeSort(array):
    '''
    check if the length of the array is greater than 1. If it is,
    then resursively run mergesort until the array is not greater
    than size 1
    '''
    if len(array)>1:
        mid = (len(array)//2)
        leftarray = array[:mid]
        rightarray = array[mid:]
        print("leftarray:{} rightarray:{}".format(leftarray, rightarray))
        #run the sort on the first half
        mergeSort(leftarray)
        #run the sort on the second half
        mergeSort(rightarray)

        '''
        At this point, we know that those mergeSorts
        will return if the if condition is not fulfilled, or 
        if the length of the array is 1. Now, we merge the lists.
        '''

        #now we have to merge based on the length of the list

        i = 0
        j = 0
        k = 0 

        '''
        First we have a while loop. The purpose of this while loop
        is to ensure that we order everything in our arrays
        when we merge them. We merge them by looking at the values
        in the left and right array, comparing them, and the lower
        one into the list to ensure that its ordered.
        '''

        #check whether or not we are still within the bounds of
        #our left and right arrays
        while i < len(leftarray) and j < len(rightarray):

            #if the value in the leftarray is less than or equal
            #to the value in the right array
            if leftarray[i] <= rightarray[j]:
                #add the value in the left array to the list
                array[k] = leftarray[i]
                i += 1
            else:
                #add the value in the right array to the list
                array[k] = rightarray[j]
                j += 1
            k += 1
        
        '''
        Now we need to handle the case where things may be left
        over. For example, if there is nothing left in the
        rightarray, then everything in the leftarray is sorted
        and larger than everything in the current array.
        '''
        while i<len(leftarray):
            array[k] = leftarray[i]
            i += 1
            k += 1
        while j<len(rightarray):
            array[k] = rightarray[j]
            j += 1
            k += 1
        return array
        '''
        At this point, we have an array where the things in the
        the array are sorted from the smaller arrays.
        '''
nums = [10, 29, 99,34, 42, 9, 22, 19, 100]
print("Beginning mergeSort")
print(mergeSort(nums))
print("End mergeSort")

def bubbleSort(array):

    '''
    A more standard sorting algorithm that essentially compares
    a value with the next value and checking to see if the value
    is higher or lower. If the current value is higher than the
    next value, then the positions are switched. Otherwise, the positions
    are kept.

    The worsecase run time would be in the event that the list is
    flipped, and is O(n^2) because of iterating through the list
    twice.
    
    we iterate through the array using range. Range with three
    parameters allows us to iterate downward, from length to 0,
    decrementing by 1 each time. Then, we create another range from
    the value of num to check each pair, up to num.
    '''
    for num in range( len(array)-1,0,-1):
        for i in range(num):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

nums = [10, 29, 99,34, 42, 9, 22, 19, 100]
print(nums)
print("Beginning bubblesort")
print(bubbleSort(nums))
print("End bubbleSort")

def quickSort(array, low, high):
    '''
    A sorting algorithm bosting O(nlogn) average runtime and O(n^2)
    worst case runtime, it is another divide and conquer sorting
    algorithm involving a pivot point.
    '''

    if low < high:
        partitionIndex = partition(array, low, high)

        quickSort(array, low, partitionIndex -1)
        quickSort(array, partitionIndex + 1, high)

def partition(array, low, high):
    '''
    The helper function for quickSort. Here, we 
    select the last element of the list as the pivot value. Then,
    we divide the list based on the pivot value, and return
    the index of the pivot value
    '''
    #select the last value as the pivot value
    pivotValue = array[high]

    #this will be used as an index for comparing values
    i = low - 1

    #iterate through the low to high values
    for j in range(low, high):
        '''
        If the value of array[j] is less than the pivot value,
        then we will 
        '''
        print("Before swap:" ,array[low:high + 1])
        if array[j] <= pivotValue:
            i += 1
            array[i], array[j] = array[j], array[i]
            print(i, j, "after swap:" ,array[low:high + 1])
    array[i + 1],array[high] = array[high], array[i + 1]
    return i + 1
nums2 = [10, 29, 99,34, 42, 9, 22, 19, 50]
print(nums2)
print("Beginning QuickSort")
print(quickSort(nums2, 0, len(nums2)-1))
print(nums2)
print("ended quickSort")










