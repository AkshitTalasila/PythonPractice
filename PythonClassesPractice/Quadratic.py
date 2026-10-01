def quadratic(coffList:list)->list:

    a = coffList[0]
    b = coffList[1]
    c = coffList[2]
    zeroOne = (((-b)+(((b*b)-4*a*c)**0.5))/(2*a))   
    zeroTwo = (((-b)-(((b*b)-4*a*c)**0.5))/(2*a))   

    zeroList = [zeroOne,zeroTwo]
    return zeroList

print(quadratic([1,5,6]))
    