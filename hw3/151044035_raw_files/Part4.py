def maxCrossingSum(arr, left, mid, right) : 
    sumOfArr = 0; leftSum = -10000
    for i in range(mid, left-1, -1) : 
        sumOfArr = sumOfArr + arr[i] 
        if (sumOfArr > leftSum) : 
            leftSum = sumOfArr 
      
    sumOfArr = 0; rightSum = -1000
    for i in range(mid+1, right+1) : 
        sumOfArr = sumOfArr + arr[i] 
        if (sumOfArr > rightSum) : 
            rightSum = sumOfArr 
      
    return leftSum + rightSum; 
  
def maxSubArraySum(arr, left, right) : 

    if (left == right) : 
        return arr[left] 
  
    mid = (left + right) // 2
    
    return max(maxSubArraySum(arr, left, mid), 
               maxSubArraySum(arr, mid+1, right), 
               maxCrossingSum(arr, left, mid, right)) 
              
    
arr = [2, 3, -40, 5, 7,-2,18,-19] 
  
maxSum = maxSubArraySum(arr, 0, len(arr) -1) 
print("Maximum contiguous sum is ", maxSum) 