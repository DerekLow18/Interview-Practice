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











