class Node:

    def __init__(self, val, node = None):
        self.val=val
        self.node=node
    

class MyLinkedList:

    def __init__(self, head: Node):
        self.head=head

    def __len__(self):
        if self.head is None: return 0
        temp: Node = self.head
        cnt=1
        while temp.node!=None:
            cnt+=1
            temp=temp.node
        return cnt
    
    def get(self):
        siz=len(self)
        if siz<=1: return None
        ind=siz*2//3-1
        temp: Node=self.head
        while ind!=0:
            ind-=1
            temp=temp.node

        return temp


    

def main():
    node4=Node(4)
    node3=Node(3, node4)
    node2=Node(2, node3)
    node1=Node(1, node2)
    head=Node(0, node1)

    linkedlist=MyLinkedList(head)

    if linkedlist.get() is not None: print(linkedlist.get().val)
    else: print("None")




if __name__=="__main__": main()



        