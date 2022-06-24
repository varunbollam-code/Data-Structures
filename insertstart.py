from pyparsing import empty


class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class LinkedList:
  def __init__(self):
    self.head=None
    
  def push_at_start(self,new_data):
      new_node=Node(new_data)
      new_node.next=self.head
      self.head=new_node    
  def print_list(self):
    if self.head is None:
      print("List is empty.")
    else:
      temp=self.head
      while(temp):
        print(temp.data)
        temp=temp.next
        
if __name__=='__main__':
  list1=LinkedList()
  list1.push_at_start(1)
  list1.push_at_start(2)
  list1.push_at_start(3)
  list1.print_list()
  
      