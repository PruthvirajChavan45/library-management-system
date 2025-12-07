import json
import random
import string
from pathlib import Path
from datetime import datetime

class Library: 

    def gen_id(Prefix = "B"): 
        random_id = ""
        for i in range(5): 
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return Prefix + "_" + random_id 

    def add_book(self): 
        title = input("Enter Book Title : ")
        author = input("Enter The Bok Author : ")
        copies = int(input("How Many Copies : "))

        book = {
            "id" : Library.gen_id(), 
            "title" : title,
            "author" : author,
            "total_copies" : copies,
            "available_copies" : copies,
            "added_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        print(book)


book_obj = Library()

print("="*50)
print("Library Management System")
print("="*50)
print("1. Add Book")
print("2. List Books")
print("3. Add Members")
print("4. List Members")
print("5. Borrow Book")
print("6. Return Book")
print("0. Exit The Portal")
print("-"*50)

choice = int(input("What Task You Want To Do : "))

if choice == 1: 
    book_obj.add_book()