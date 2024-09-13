class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.length = 1
        # pagenum represents the index of the current page in the list
        self.pagenum = 1
        self.cur = ListNode(homepage, None, None)
        

    def visit(self, url: str) -> None:
        # forward history is cleared up so end of list becomes current page
        self.length = self.pagenum + 1
        self.pagenum += 1
        # set the next page of the current page to url
        self.cur.next = ListNode(url, None, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        counter = 0
        while counter < steps and self.pagenum > 1:
            self.cur = self.cur.prev
            self.pagenum -= 1
            counter += 1
        
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        counter = 0
        while counter < steps and self.cur.next is not None:
            self.cur = self.cur.next
            self.pagenum += 1
            counter += 1
        
        return self.cur.val
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

'''
browser -> start on homepage, visit another url, move forward or backward x steps

1. BrowserHistory(homepage) - initialize the object with the hompage of the browser
2. visit(url) - visits url from the current page
    - clears up all the forward history
3. back(steps) - move steps back in history
    - if you can only return x steps in the history and steps > x then only return x steps
4. forward(steps) - move steps forward in history
    - if you can only return x steps in the history and steps > x then only return x steps

doubly linked list implementation where val is a string -> O(n) back and forward
visit should set cur.next to new page
'''