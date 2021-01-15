class Node(object):

    def __init__(self,value):
        self.value = value
        self.next_node:None


class LinkedList(object):

    def __init__(self,head=None):
        if head:
            self.head = Node(head)
        else:
            self.head = None


    def insert(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            self._insert(self.head,value)


    def _insert(self,current_node,value):
        if current_node.next_node == None:
            current_node.next_node = Node(value)
        else:
            self._insert(current_node.next_node,value)


    def delete(self,value):
        if self.head == None:
            return 
        elif self.head.value == value:
            self.head = None
        else:
            self._delete(self.head,value)


    def _delete(self,current_node,value):
        if current_node.value == value:
            current_node = current_node.next_node
        else:
            self._delete(current_node.next_node,value)


    def print_list(self):
        if not self.head:
            print("Empty!!")
        else:
            current = self.head
            while current:
                print(current.value)
                current = current.next_node



    def search(self,value):
        if not self.head:
            return "Empty!!"
        return self._search(self.head,value)


    def _search(self,current_node,value):
        if current_node == None:
            return
        elif current_node.value == value:
            return current_node
        return self.search(current_node.next_node,value)





    
               




