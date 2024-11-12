def main():
    try:
        # Initialize books List
        booksList = []
        with open("theBooksList.txt", "r") as infile:
            line = infile.readline()
            while line:
                booksList.append(line.rstrip("\n").split(","))
                line = infile.readline()

    except FileNotFoundError:
        print("The <booksList file.txt> is not found.")
        print("Starting a new books list!")
        booksList = []
    
    choice = 0
    while choice != 5:
        print("*** Books Manager ***")
        print("1. Add a Book")
        print("2. Details of a book")
        print("3. Display books")
        print("4. Delete a book")
        print("5. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Adding a book.....")
            nBook = input("Enter the name of the book: ")
            nAuthor = input("Enter the name of the author: ")
            nPages = input("Enter the number of pages: ")
            nPrice = input("Enter the price of the book: ")

            booksList.append([nBook, nAuthor, nPages, nPrice])

        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter the name of the book: ")
            found = False
            for book in booksList:
                if keyword.lower() in book[0].lower():  # case-insensitive search for book title
                    print(book)
                    found = True
            if not found:
                print("No book found with that title.")

        elif choice == 3:
            print("Displaying all books....")
            if booksList:
                for i, book in enumerate(booksList):
                    print(f"{i+1}. {book[0]} by {book[1]} ({book[2]} pages, ${book[3]})")
            else:
                print("No books in the list.")

        elif choice == 4:
            print("Deleting a book....")
            delete_title = input("Enter the name of the book to delete: ")
            found = False
            for i, book in enumerate(booksList):
                if delete_title.lower() == book[0].lower():  # case-insensitive comparison
                    del booksList[i]
                    print(f"Deleted book: {book[0]}")
                    found = True
                    break
            if not found:
                print(f"No book found with the title '{delete_title}'.")

        elif choice == 5:
            print("Quitting Program")
    
    print("Program Terminated")

    # Saving the books to the external file
    with open("theBooksList.txt", "w") as outfile:
        for book in booksList:
            outfile.write(",".join(book) + "\n")

if __name__ == "__main__":
    main()
