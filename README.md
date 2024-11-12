# Task-Manager project
Here's a detailed description of your book management system code, which is designed to manage a collection of books by allowing the user to add, search, display, delete, and save book records.

Project Overview
This program is a Books Manager application, which lets users:

Add a new book record with details such as title, author, number of pages, and price.
Retrieve information about a specific book by searching for its title.
Display all books currently in the collection.
Delete a book record by specifying its title.
Save any updates to a file (theBooksList.txt) for future use.
The program maintains book records in a list and reads from/writes to an external file for persistent storage.

Code Walkthrough
1. Initialization and File Handling
The program starts by trying to open theBooksList.txt, where existing book records are stored:
If the file exists, each line is read and split by commas to populate booksList.
If the file is not found, it alerts the user and initializes booksList as an empty list, allowing the user to start a new collection.

2. Main Menu and User Input
The program runs a loop with the following menu options:

i. Add a Book: Prompts the user to enter details about the book (title, author, number of pages, and price) and appends this information as a list to booksList.

ii. Details of a book: Prompts the user to enter a book title keyword, searches for it within booksList, and prints any matches (case-insensitively). If no match is found, a message is displayed.

iii. Display books: Displays all books in booksList in a formatted manner, showing the book title, author, number of pages, and price.

iv. Delete a book: Prompts the user to enter a book title, finds the exact match and removes the corresponding entry from booksList. If no match is found, a message is shown.

v. Quit: Exits the program after saving the updated booksList back to theBooksList.txt.

4. Saving Book Data
When the user chooses to quit, the program writes each book record from booksList back to theBooksList.txt, saving any changes made during the session.

Example Run
An example interaction might look like this:

The user selects "1. Add a Book," enters the title "To Kill a Mockingbird," author "Harper Lee," pages "281," and price "12.99".

The user selects "3. Display books" to see all the added books.

The user selects "2. Details of a book," enters the keyword "Mockingbird," and sees the details for "To Kill a Mockingbird."

The user selects "4. Delete a book" and enters "To Kill a Mockingbird," removing it from the list.

Finally, the user selects "5. Quit" to end the session, with any added or modified books saved to theBooksList.txt.

Key Features

Persistence: Saves data to a text file for use in later sessions.

Case-insensitive search and delete: Enables user-friendly search and deletion.

User-friendly prompts and structured display: Provides clear instructions and formatting for ease of use.

