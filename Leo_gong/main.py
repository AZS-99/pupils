import math

from data_structure.Node import Node




if __name__ == '__main__':

   n1 = Node(10)
   n2 = Node(20)
   n3 = Node(30)

   n2.nxt = n3
   n1.nxt = n2

   current = n1
   while current.nxt != None:
       current = current.nxt
   print(current)


