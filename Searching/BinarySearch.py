def BinarySearch(nums, num):
    low = 0
    high = len(nums) - 1
    
    while(low <= high):
        mid = low + (high-low)//2 
        
        if nums[mid] == num:
            return mid
        elif(nums[mid] > num):
            high = mid - 1
        else:
            low = mid + 1
    return -1
    
def BinarySearchRecursion(nums, low, mid, high, num):
  
