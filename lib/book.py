#!/usr/bin/env python3

class Book:
    def __init__ (self,title,page):
        self.title = title
        self.page_count = page
    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self,pageCount):
        if isinstance(pageCount, int):
            self._page_count = pageCount
        else:
            print("page_count must be an integer") 
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        

