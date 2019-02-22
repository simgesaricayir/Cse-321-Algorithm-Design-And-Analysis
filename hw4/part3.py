import heapq

def mergeK(arrays):
    heap = []
    for i in range(len(arrays)):
        heap.append((arrays[i][0], i, 0))#append every array's first index into the heap
    heapq.heapify(heap) #Transform list heap into a min-heap, in-place, in linear time
    merged = [] #array that holds result of merged arrays
    while heap:
        val, index_array, index_elem = heapq.heappop(heap)#assign popped elements values
        merged.append(val)# add value to the merged array
        if index_elem + 1 < len(arrays[index_array]):
            heapq.heappush(heap, (arrays[index_array][index_elem + 1],index_array, index_elem + 1))
            #push the item to the given min-heap at the parameter
    return merged

arrayOfArrays = [[1, 5, 7, 11], [2, 3, 4, 8], [5, 6, 9, 12],[-9,-4,16,45]]
print (mergeK(arrayOfArrays))
