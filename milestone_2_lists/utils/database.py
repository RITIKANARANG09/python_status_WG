import json
#import sqlite3
"""
Concerned for storing and retrieving books from a list
"""
# books=[]
#
# def add_book(name,author):
#     books.append({'name':name,'author':author,'read':False})
#
# def get_all_books():
#     return books
#
# def mark_book_as_read(name):
#     for book in books:
#         if book['name']==name:
#             book['read']=True
#
# def delete_book(name):
#     global books
#     books=[book for book in books if(book['name']!=name)]
# #not a good idea bcs while iterating we shouldn't delete a list as python will get lil bit confused
# # def delete_book(name):
# #     for book in books:
# #         if book['name']==name:
# #             books.remove(book)


"""CSV"""
# books_file="books.txt"
#
# def create_book_table():
#     with open('books.txt','w'):
#         pass
# def add_book(name,author):
#     with open(books_file,'a') as file:
#         file.write(f'{name},{author},0')
#
# def get_all_books():
#     with open(books_file,'r') as file:
#         lines=[line.strip().split() for line in file.readlines()]
#
#     return [
#         {
#             'name':line[0],
#             'author':line[1],
#             'read':line[2]
#         }
#         for line in lines
#     ]
#
# def mark_book_as_read(name):
#     books=get_all_books()
#     for book in books:
#         if book['name']==name:
#             book['read']='1'
#     _save_all_books(books)
#
# def _save_all_books(books):
#     with open(books_file,'w') as file:
#         for book in books:
#             file.write(f'{book['name']},{book['author']},{book['read']}\n')
#
# def delete_book(name):
#     books=get_all_books()
#     books=[book for book in books if book['name']!=name]
#     _save_all_books(books)

"""JSON"""
# books_file="books.txt"
#
# def create_book_table():
#     with open('books.txt','w') as file:
#         json.dump([],file)
#
# def _save_all_books(books):
#     with open(books_file,'w') as file:
#         json.dump((books,file))
#
# def add_book(name,author):
#     books=get_all_books()
#     books.append({'name':name,'author':author,'read':False})
#     _save_all_books(books)
#
# def get_all_books():
#     with open(books_file,'r') as file:
#         return json.load(file)
#
# def mark_book_as_read(name):
#     books=get_all_books()
#     for book in books:
#         if book['name']==name:
#             book['read']=True
#     _save_all_books(books)
#
# def delete_book(name):
#     books=get_all_books()
#     books=[book for book in books if book['name']!=name]
#     _save_all_books(books)
from .database_connection import DatabaseConnection
"""sqlite3"""
def create_book_table():
     with DatabaseConnection('data.db') as connection:

          cursor=connection.cursor()
          cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name,author):
     with DatabaseConnection('data.db') as connection:
          cursor=connection.cursor()

          cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))


def get_all_books():
     with DatabaseConnection('data.db') as connection:
          cursor=connection.cursor()
          cursor.execute('SELECT * FROM books')
          books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # list of tuples

     return books

def mark_book_as_read(name):
     with DatabaseConnection('data.db') as connection:
          cursor=connection.cursor()

          cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))

def delete_book(name):
     with DatabaseConnection('data.db') as connection:
          cursor=connection.cursor()

          cursor.execute('DELETE FROM books Where name=?',(name,))



