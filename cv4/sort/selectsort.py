#indikátor setřízenosti je vždy před dalším polem v seznamu, které není setřízené 
#žádné dotazy? tak to napište

#co že to dělám? řadím následující seznam:
alist = ["v", "d", "a", "z"]

#inicializace proměnných
min = alist[0]
ind = 0

#while ind < len(alist):
#for i in range (len(alist)):   

for (idx, val) in enumerate(alist):
    if val < min:
        min = val        #nastavení minima
        idx_min = idx    #index minima 

        temp = alist[ind]
        alist[ind] = alist[idx_min]
        alist[idx_min] = temp
        
    ind += 1 


print(alist)