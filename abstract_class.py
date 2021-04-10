class Book:
    def __init__(self,a,Author,Price):
        self.Title=a
        self.Author=Author
        self.Price=Price
a=raw_input()
Author=raw_input()
Price=raw_input()
print("Title:"+" " +a)
print("Author:"+" " +Author)
print("Price: " +Price)

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook():
    def __init__(self,title,Author,Price):
        self.title=title
        self.author=author
        self.price=price




    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))    
  

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()