def Search(inputArray, left, right): # search the given array with binary search tecnique 
    if right >= left: 
        mid = (left + right)//2
    if mid == inputArray[mid]: #if index number is equal to data in that index return it.
        return mid   
    elif mid > inputArray[mid]: 
        return Search(inputArray, (mid + 1), right) 
    else: 
        return Search(inputArray, left, (mid -1)) 
    return -1#if it could not found return -1 
  
arr = [-14, 17, 0, 8, 4, 11, 33, 67, 25,98] 
print("Fixed Point is " ,(Search(arr, 0, len(arr)-1))) 