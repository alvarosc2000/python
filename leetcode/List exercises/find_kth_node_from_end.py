class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  

  
 
  
def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    # Mover fast k pasos adelante
    for _ in range(k):
        if fast is None:
            return None  # Lista demasiado corta
        fast = fast.next

    # Mover ambos punteros hasta que fast llegue al final
    while fast:
        slow = slow.next
        fast = fast.next

    return slow  # Retorna el nodo, o usa slow.value si quieres el valor

    





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

