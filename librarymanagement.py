# library management code
# These are the books in the library you can edit this to add your books or change it
books = ["sst","math","english","history","computer","hindi","geography","sanskrit"]#ypu can edit this according to you
takenbooks = []
print("Welcome to my School Library")
while True:
    print("1.see the available books")
    print("2.issue a book")
    print("3.return your book")
    print("4.see the book that are issued")
    print("5.leave")
    choice = int(input("enter your choice: "))
    if choice == 1:
        print("the books in the library are")
        for book in books:
            print('the books are',book)
        print("number of the books in the library are", len(books))
    elif choice == 2:
        print("the available books are")
        for book in books:
            print(book)
        want = input("which book do you want to issue ")
        if want in books:
            books.remove(want)      # removing the book from school library
            takenbooks.append(want)  # the book is added to the list that states the book is taken
            print("the book is issued to you")
        else:
            print("this book is not in the library")   
    elif choice == 3:
        if len(takenbooks) == 0:
            print("you have not taken any book right now")
        else:
            print("the Taken Books are")
            for book in takenbooks:
                print(book)
            back = input("Which book are you returning to library ")
            if back in takenbooks:
                takenbooks.remove(back)
                books.append(back)
                print("the book is returned")
            else:
                print("you did not issue this book")        
    elif choice == 4:
        print("the books that are already taken by students are")
        if len(takenbooks) == 0:
            print("No book is taken")
        else:
            for book in takenbooks:
                print(book)     
    elif choice == 5:
        print("bye")
        break 
    else:
        print("you entered the wrong number")
