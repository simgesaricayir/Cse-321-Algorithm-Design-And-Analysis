def OptimalPlan(ListNy,ListSf,M):
    PlanN,temp,PlanS= ListNy[0],ListNy[0],ListSf[0]
    for i in range(1,len(ListNy)):
        PlanN = ListNy[i] + min(temp,M+PlanS)
        PlanS = ListSf[i] + min(PlanS,M+temp)
        temp = PlanN
    return min(PlanN,PlanS)

ListNy = [10,5,10,5]
ListSf = [5,10,5,10]
print(OptimalPlan(ListNy,ListSf,10))
ListNy = [1,3,20,30]
ListSf = [50,20,2,4]
print(OptimalPlan(ListNy,ListSf,10))