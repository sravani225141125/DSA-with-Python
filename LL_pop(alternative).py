class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    ### WRITE POP METHOD HERE ###
    def pop(self) :
        if self.length==0:
            return None
       if self.length==1:
         temp = self.head
         self.head=None
         self.tail=None
         self.length-=1
         return temp
       else:
         temp=self.head
         while(temp.next.next is not None) :
           temp=temp.next
         last_node=temp.next
         temp.next=None
         self.tail=temp
         self.length -=1
         return last_node
          


           

my_linked_list=LinkedList(1)
my_linked_list.append(2)
# 2 Items - returns 2 Node
print(my_linked_list.pop())
# 1 Item - returns 1 Node
print(my_linked_list.pop())
# 0 Item - returns None
print(my_linked_list.pop())

        



 
