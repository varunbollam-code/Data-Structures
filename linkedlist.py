class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList():
  def __init__(self):
    self.head=None
    
  def printlist(self):
    if self.head is None:
      print("List is empty.")
    else:
      temp=self.head
      while(temp):
        print(temp.data)
        temp=temp.next
if __name__=='__main__':
  list1=LinkedList()
  list1.head=node(1)
  second=node(2)
  third=node(3)
  fourth=node(4)
  list1.head.next=second
  second.next=third
  third.next=fourth
  list1.printlist()