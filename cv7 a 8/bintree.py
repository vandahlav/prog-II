#degradovaný halda = strom(?) - prostě taková dlouhá housenka, strom nemá větvění (pokus o vizuální reprezentaci: O-O-O-O-O-O)
#co s tím? každý vrchol bude objekt, který si bude pamatovat data (aka číslo v něm uložené)
#co si bude pamatovat strukturu stromu? potřebuju si pamatovat left and right sibling a pak i parent --> další třídou, který bude reprezentovat ten strom

class Node(object): 
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        #id fce vrátí unikátní hodnotu, zjistím, jestli ten bod je stejný nebo jen jestli mají stejnou hodnotu
        return f"Node {id(self)}: {self.data}, left: {id(self.left)}, right: {id(self.right)}, parent: {id(self.parent)}."

n1 = Node(1)
n2 = Node(2)

print(id(None)) #abych later věděla, že to je prázné 
print(n1)
print(n2)

n1.right = n2
n2.parent = n1
print(n1)
print(n2)