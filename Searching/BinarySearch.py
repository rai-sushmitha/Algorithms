#Iterative method
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

#Recursive method
def BinarySearchRecursion(nums, low, high, num):
    if(high >= low):
        mid = low + (high-low)//2
        
        if nums[mid] == num:
            return mid

        elif(nums[mid] > num):
            return BinarySearchRecursion(nums, low, mid - 1, num)
        else:
            return BinarySearchRecursion(nums, mid + 1, high, num)
    else:
        return -1

    
  
