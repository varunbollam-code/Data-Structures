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
    
  def after(self,pos_data,data):
    ref=self.head
    while ref is not None:
      if pos_data==ref.data:
        break
      ref=ref.next
    if ref is None:
      print('list as empty')
    else:
      new_node=Node(data)
      new_node.next=ref.next
      ref.next=new_node
      
  def end(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
    else:
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      temp.next=new_node
  
  def printlist(self):
    temp=self.head
    if temp is None:
      print('list is empty')
    else:
      while temp is not None:
        print(temp.data)
        temp=temp.next
        
ll1=LinkedList()
ll1.push(1)
ll1.push(2)
ll1.push(3)
ll1.push(4)
ll1.end(5)
ll1.after(3,6)
ll1.printlist()
