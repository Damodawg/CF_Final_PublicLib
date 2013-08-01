#The following was written by Damian Wylie on 8/1/2013

import sys

class library(object):


    def __init__(self):
        #defines the library dictionary
        self.my_dict = {}

    def up_date(self,book_name, shelf):
        #this function adds book & shelf information to the library dictionary
        self.my_dict[book_name] = shelf
        print ('Your book "' + str(book_name) + ('" was stored on shelf ') + str(shelf))

    def checkout(self,del_book):
        #this function allows the user to checkout books from the library
        for key,value in self.my_dict.items():
            if key == del_book:
                temp_key = key
                temp_value = value
                del self.my_dict[del_book]
                print (str(temp_key) + " was checked out from shelf " + str(temp_value))
                break
            else:
                #Returns false to convey book could not be found
                return False

    def show_books(self):
        #allows the user to see all the books in the library and respective locations
        count = 0
        for key, value in self.my_dict.items():
            print (str(key) + " on shelf " + str(value))
            count +=1
        #I used count here to trigger the response "no books available" by returning 0
        if count == 0:
            print("******************************************************")
            print("I'm sorry, we have no books available for checkout :-P ")
            print("******************************************************")
            return 0

    def check_inventory(self,book_name):
        #checks for inventory.  If's its found function returns book name
        for key, value in self.my_dict.items():
            if key == book_name:
                print ('I found the book "' + str(key) + '" on shelf ' + str(self.my_dict[book_name]))
                return book_name


inventory = library()
#Mamma function which calls other functions in library class
def bookkeeper(add_book, inventory):

    if add_book.lower() == 'add':
        book_name =  input ('What is the name of the book?  ')


        found_inventory = inventory.check_inventory(book_name)

        if found_inventory == book_name:
            print ("I'm sorry, Damo's library does not accept duplicate books.  Please rename or check in another book")
            return False
        else:
            return book_name

    if add_book.lower() == 'rem':
        result = inventory.show_books()
        if result == 0:

            return False

        book_remove = input('This is our inventory.  Which book would you like to checkout?  ')

        result_chk = inventory.checkout(book_remove)

        if result_chk == False:
            print (book_remove + " could not be found")
            return False
        else:
            return False
    if add_book.lower() == 'brow':
        inventory.show_books()

        return False

    elif add_book.lower() =='exit':
        print ("Thank you come again!")
        sys.exit()

    else:
        print ("Ok, let me know when you are ready")
        return False

while True:
    print("***************************************************************************************************")
    add_book = input("Welcome to Damo's library.  Would you like to add (add), remove (rem), or browse (brow)? (type exit to exit) ")
    print("***************************************************************************************************")
    book_name = bookkeeper(add_book,inventory)

    if book_name != False:
        shelf_id = input('What shelf does it belong to? ')

        inventory.up_date(book_name,shelf_id)
