alist = ["v", "d", "a", "z", "b", "p", "a"]

#napsat fci "prohoď", která prohodí prvky v alist tak, aby prvky před pivotem byly < a ty za >
def swap (alist: list, l:int, r:int, pivot) -> tuple:
    while l < r:
        while alist[l] < pivot:
            l += 1

        while alist[r] > pivot:
            r -=1

        if l > r:
            return l, r
        temp = alist[l]
        alist[l] = alist[r]
        alist[r] = temp  
        l+=1        #nebude pak l a r too big pro seznam??
        r-=1

    return l, r

#postup QuickSort: kontrola, zvolit pivota, swap, qs na levou stranu, qs na pravou stranu
 
def quickSort (alist:list, l:int, r:int):
    
    if r - l <= 0:      #podmínka, kdy má rekurze skončit, jinak to běží pořád dokola
        return

    pivot = alist[int((l + r) / 2)]
    i, j = swap (alist, l, r, pivot)    #swap vrací i a j prohozené 

    quickSort(alist, l, j)  #třídí levou stranu
    quickSort(alist, i, r)  #třídí pravou stranu
    
quickSort (alist, 0, (len(alist)-1))
print(f"Seřazený seznam: {alist}.")
