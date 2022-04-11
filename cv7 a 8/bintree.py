#degradovaná halda = strom(?) - prostě taková dlouhá housenka, strom nemá větvení (pokus o vizuální reprezentaci: O-O-O-O-O-O)
#co s tím? každý vrchol bude objekt, který si bude pamatovat data (aka číslo v něm uložené)
#co si bude pamatovat strukturu stromu? i need to remember left and right sibling a pak i parent --> další třídou, který bude reprezentovat ten strom

class Node(object): 
    def __init__(self, data) -> None:
        self.data = data
        self.left : Node = None
        self.right : Node = None
        self.parent : Node = None

    def __str__(self):
        #id fce vrátí unikátní hodnotu, zjistím, jestli ten bod je stejný nebo jen mají stejnou hodnotu
        return f"Node {id(self)}: {self.data}, left: {id(self.left)}, right: {id(self.right)}, parent: {id(self.parent)}."

class BinaryTree(object):
    def __init__(self) -> None:
        self.root : Node = None

    def __str__(self) -> str:
        return f"BinaryTree {id(self)}: root: {id(self.root)}."

#NAPIŠTĚ BINÁRNÍ VYHLEDÁVACÍ TREE
class BinarySearchTree(BinaryTree):

    #vloží prvek do stromešku
    def insert(self, data) -> None:
        if self.root == None:
            self.root = Node(data)  #data jsou většinou str, musím z nich udělat node

        #je lepší si pamatovat objekt, ne hodnotu - můžu se pak ptát na kiddos
        cur_data = self.root 

        while self.root != None:    #nekonečný cyklus, protože nevím, kolik toho tam je 
            if cur_data.data < data: 
                if cur_data.right != None:
                    cur_data = cur_data.right
                else:
                    cur_data.right = Node(data)     #vytvářím objekt, takže dát do node
                    return       #lepší mít return tady, asi by to skončilo u posledního ifu, ale tohle je better
            
            if cur_data.data > data:
                if cur_data.left != None:
                    cur_data = cur_data.left
                else:  
                    cur_data.left = Node(data)
                    return

            if cur_data.data == data:
                return                  
            
    #ptá se, jestli daný prvek je in the tree
    def query (self, data) -> bool: 
        if self.root == None:
            return False

        cur_data = self.root 

        while self.root != None:   
            if cur_data.data > data: 
                if cur_data.right != None:
                    cur_data = cur_data.right
                else:
                    return False
            
            if cur_data.data < data:
                if cur_data.left != None:
                    cur_data = cur_data.left
                else:  
                    return False

            if cur_data.data == data:
                return True

n1 = Node(1)
n2 = Node(2)

print(f"id of nothingness: {id(None)}.")

#samostatné objekty
print(n1)
print(n2)

#propojení stromu
n1.right = n2
n2.parent = n1
print(n1)
print(n2)

tree = BinaryTree()
tree.root = n1
print(tree)