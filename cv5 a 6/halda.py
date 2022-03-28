def lchild(me:int):
    return me*2

def rchild(me:int):
    return me*2 + 1

def parent(me:int):
    return me//2 

#let's be fancy and make a fuction for swaping
def swap (heap, child, rodic):
    temp = heap[rodic]
    heap[rodic] = heap[child]
    heap[child] = temp

def insert (heap: list, item):
    heap.append(item)       #přidá prvek na konec haldy
    fixUp(heap)             #spravit haldovou podmínku - aby halda dávala šmyšl

# how?
# dokud nejsem v kořeni, končím
#       podívám se na rodiče
#       pokud je rodič menší než já, končím
#       jinak 
#         prohodím rodiče s menším ze synů
#         posunu se na pozici rodiče
#       a pokračuju od začátku
# fun(?) fact: levé child je sudé, sudé je vlevo

def fixUp (heap):   #nemusím mu dávat další parametr, vím, že broken je ten poslední prvek
    item_t = len(heap) - 1  #index posledního prvku (ten, co přidávám)

    #dokud nejsem v kořeni, probíhá spravování haldy
    while item_t > 1:   
        rodic = parent(item_t)

        #porovnávám hodnoty, NE indexy
        if heap[rodic] < heap[item_t]:  
            return

        #tohle je, že já jsem vlevo - takže můj index je menší(sudý)
        if item_t % 2 == 0: 

        #potřebuju moji a sourozencovu hodnotu, abych mohla prohazovat
            me = heap[item_t]
            if item_t + 1 > len(heap) - 1:
                swap(heap, item_t, rodic)   #šlo by vložit i fci do fce (jako parent)
                item_t = rodic 
                continue
            
            sis = heap[item_t + 1]
            if sis <= me: 
                swap(heap, item_t + 1, rodic)
            else:
                swap(heap, item_t, rodic) #přiřazuju item_t ne me, protože potřebuju fci dát indexy 

        #já jsem vpravo - tedy mám větší index
        else:      
            sis = heap[item_t - 1]
            me = heap[item_t]
            if sis <= me: 
                swap(heap, item_t - 1, rodic)
            else:
                swap(heap, item_t, rodic)

        #posunu se, aby teď můj index byl index rodičův - vztahuje se k podmínce upsies
        item_t = rodic

halda = [0,1,3,5,6,4,10,11,16,20,9,8]
insert(halda, 2)
print(f"Sežazená halda: {halda}.")