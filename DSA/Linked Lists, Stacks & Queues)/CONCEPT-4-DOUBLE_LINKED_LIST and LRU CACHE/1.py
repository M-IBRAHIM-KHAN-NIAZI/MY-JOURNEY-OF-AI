# LeetCode 1472: Design Browser History
class node:
    def __init__(self,url):
        self.url=url
        self.prev=None
        self.next=None

class browserhistory:
    def __init__(self,homepage):
        self.head=node(homepage)
        self.current=self.head

    def visit(self,url):
        new_node=node(url)
        self.head.next=new_node
        new_node.prev=self.head

        self.current=new_node

    def back (self,steps):
        while steps>0 and self.current.prev:
            self.current=self.current.prev
            steps-=1
        return self.current.url

    def forward(self,steps):
        while steps>0 and self.current.next:
            self.current=self.current.next
            steps-=1
        return self.current.url        



                
        