class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node=Node(data)
        new_node=self.head
        self.head=new_node
    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node 
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def insert_values(self,d_list):
        self.head=None
        for data in d_list:
            self.insert_at_end(data)
         

    def get_length(self):
        count=0
        a=self.head
        while a:
            count+=1
            a=a.next
        return count
    def insert_after_value(self,data_after,data_to_insert):
        a=self.head
        while a:
            if a.data==data_after:
                break
            a=a.next
        if a is None:
            raise Exception("Value not found")
        new_node=Node(data_to_insert)
        new_node.next=a.next
        a.next=new_node
    def get_length(self):
        count=0
        a=self.head
        while a:
            count+=1
            a=a.next
        return count
    def remove(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        a=self.head
        count=0
        while a:
            if count==index-1:
                a.next=a.next.next
                break
            a=a.next
            count+=1
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        a=self.head
        while a.next:
            if a.next.data==data:
                a.next=a.next.next
                return
            a=a.next


ll=LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.display()
ll.insert_after_value("mango","apple")
ll.display()
ll.remove_by_value("orange") # remove orange from linked list
ll.display()
ll.remove_by_value("figs")
ll.display()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.display()
