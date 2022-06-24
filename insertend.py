class Node:
  def __init__(self,data):
    self.data=data
    self.next=None 

class LinkedList:
  
  def __init__(self):
    self.head=None
  
  def push(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node
  
  def insert_end(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
    else:
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      temp.next=new_node
  
  def printlist(self):
    if self.head is None:
      print('list is empty.')
    else:
      temp=self.head
      while(temp):
        print(temp.data)
        temp=temp.next
        
list1=LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.insert_end(10)
list1.printlist()

  
