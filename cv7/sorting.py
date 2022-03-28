import heapq

data = [{"name:": "Anna", "age": 15}, {"name": "Bedřich", "age": 10}]

def name (item):
    return item['name']

def age (item):
    return item['age']

print(data)

#zkratka pro funkce nad tímhle
#určeno pro určitá místa, kdy to prostě potřebuju seřadit
#třídí se podle klíče; lambda fce
data.sort(key = lambda it : it ['age'])
print(data)

#pro haldu modul heapq - nutné importovat
#nemá parametr key - nevýhoda