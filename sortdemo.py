# -*- coding: utf-8 -*-

# 17.02.2023
# 
#
# source
# https://medium.com/analytics-vidhya/a-basket-of-sorting-algorithms-using-python-84a6c43f6aba
# 

import random
import time

#
# Bubble sort
#


def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    
    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            
            # 2. Compare the number with  
            if nums[i] > nums[i+1]:
                
                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums
  
#
# Insertion sort
#
    
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums

#
# Mergesort
#
    
def merge(nums1, nums2):    
    # List to store the results 
    merged = []
    
    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):        
        
        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1 
        else:
            merged.append(nums2[j])
            j += 1
    
    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    # Return the final merged array
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums

#
# Quicksort
# 

def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    l, r = start, end-1
    
    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        
        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
    
def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums
   
    
    
if __name__ == '__main__':
    
    # 
    #
    amount = 20000
    #
    print("starting generating testdata...")
    randoms = [ random.randint(1,10000000) for i in range(amount) ]
    print("done")
    print (" ")
    start = time.time()
  
    # 
    # bubble sort
    #
    randomwork = randoms[:]
    start = time.time()
    bubble_sort(randomwork)
    stop = time.time() - start
    print("bubble sort \t\t\t\t"+ str(stop))
    # 
    # insertion sort
    #
    randomwork = randoms[:]
    start = time.time()
    insertion_sort(randomwork)
    stop = time.time() - start
    print("insertion sort \t\t\t"+ str(stop))      
    # 
    # merge sort
    #
    randomwork = randoms[:]
    start = time.time()
    merge_sort(randomwork)
    stop = time.time() - start
    print("merge sort \t\t\t\t"+ str(stop))   
    # 
    # quicksort
    #
    randomwork = randoms[:]
    start = time.time()
    quicksort(randomwork)
    stop = time.time() - start
    print("quicksort \t\t\t\t"+ str(stop))    
    # 
    # build in sort
    #
    randomwork = randoms[:]
    start = time.time()
    randomwork.sort()
    stop = time.time() - start
    print("python build in sort\t\t"+ str(stop))     
    

    
    
    
    
   

  