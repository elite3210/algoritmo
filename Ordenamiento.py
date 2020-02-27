lista = [5,3,7,9,1,0,2,5,3,7,10,8]

def mergeSort(lista):
    mitad = len(lista)//2
    lft = lista[:mitad]
    rgt = lista[mitad:]
    if len(lft) > 1:
        lft = mergeSort(lft)
    if len(rgt) > 1:
        rgt = mergeSort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

print(mergeSort(lista))