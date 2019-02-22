from math import pow
def optimalSequence(inputL):
    hotel = inputL
    bestpath =[None]*len(hotel)
    stop = [None]*len(hotel)
   
    for i in range(0,len(hotel)):
        bestpath[i] = math.pow(200-hotel[i],2)
        stop[i]=0
        for j in range(0,i):
            if bestpath[j]+math.pow(200-hotel[i]+hotel[j],2) <bestpath[i]:
                bestpath[i] = bestpath[j]+math.pow(200-hotel[i]+hotel[j],2)
                stop[i]= j+1
 
    finalPath = ""
    index = len(stop)-1
    while (index >=0):
        finalPath = str(index+1)+" "+finalPath
        index = stop[index] -1
    return finalPath
    
print(optimalSequence([190, 220, 410, 580, 640, 770, 950, 1100, 1350]))

