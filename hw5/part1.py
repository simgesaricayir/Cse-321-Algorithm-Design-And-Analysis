def process(Jobs): 
    weightedSum =0
    weightedT=0
    index =0
    for i in range(len(Jobs)):
        minPos = i
        for j in range(i+1, len(Jobs)):
            if Jobs[minPos][1] < Jobs[j][1]:
                minPos = j
       
        temp = Jobs[i]
        Jobs[i] = Jobs[minPos]
        Jobs[minPos] = temp
    while(index < len(Jobs)): #after the descending order sort weighted sum is calculated with loop
        weightedT = Jobs[index][0] + weightedT
        weightedSum = weightedSum + Jobs[index][1]*weightedT
        index = index +1
    print(Jobs)
                
    return weightedSum
    
    
    
Jobs = [[1,10],[3,5],[4,7],[2,11],[1,15]]# first t and second w
print(process(Jobs))
Jobs = [[5,2],[1,5],[4,9],[2,11]]# first t and second w
print(process(Jobs))
Jobs = [[3,2],[1,10]]# first t and second w
print(process(Jobs))
Jobs = [[2,3],[1,10],[3,5]]# first t and second w
print(process(Jobs))