class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  
  def __init__(self):
    self.head=None
     
  def insert_after(self,x,data):
    ref=self.head
    while ref is not None:
      if x==ref.data:
        break
      ref=ref.next
    if ref is None:
      print("That data node is not present in the List.")
    else:
      new_node=Node(data)
      new_node.next=ref.next
      ref.next=new_node
  def printlist(self):
    if self.head is None:
      print("list is empty.")
    else:
      temp=self.head
      while(temp):
        print(temp.data)
        temp=temp.next
      
if __name__=='__main__':
  ll1=LinkedList()
  ll1.head=Node(1)
  second=Node(2)
  third=Node(4)
  ll1.head.next=second
  second.next=third
  ll1.insert_after(2,3)
  ll1.printlist()
  
      
     