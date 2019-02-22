def IsSatisfiable(array,constraints):
    for eq in constraints[0]:  # equality constraints check
        if array[eq[0]]!= array[eq[1]]:
            return False
    for eq in constraints[1]: # inequality constraints check
        if array[eq[0]]== array[eq[1]]:
            return False   

    return True
array = [2,5,6,2]
constraints = [[(0,3)],[(1,2)]] # 0,3 is equality constraint index and 1,2 is inequality constraint indexes
print(IsSatisfiable(array,constraints))
print()
array = [2,5,6,2,6,5]
constraints = [[(0,3),(1,5)],[(2,4)]]  #(0,3),(1,5) are equality constraint and (2,4) is inequality constraint
print(IsSatisfiable(array,constraints))
print()
array = [2,11,6,11,6,11,9,11]
constraints = [[(5,3),(1,5),(7,1)],[(2,3),(0,7)]] #(5,3),(1,5),(7,1) are equality constraint and (2,3),(0,7) are inequality constr.
print(IsSatisfiable(array,constraints))