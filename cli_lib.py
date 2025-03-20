import json

class PersonalLibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        """Load the library from a file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_library(self):
        """Save the library to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        """Add a new book to the library."""
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        year = int(input("Enter publication year: "))
        genre = input("Enter genre: ").strip()
        isbn = input("Enter ISBN number: ").strip()
        barcode = input("Enter Barcode: ").strip()
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        
        book = {"title": title, "author": author, "year": year, "genre": genre, "isbn": isbn, "barcode": barcode, "read": read_status}
        self.library.append(book)
        self.save_library()
        print("Book added successfully!\n")

    def remove_book(self):
        """Remove a book from the library by title."""
        title = input("Enter the title of the book to remove: ").strip()
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        self.save_library()
        print("Book removed successfully!\n")

    def search_book(self):
        """Search for a book by title, author, ISBN, or Barcode."""
        keyword = input("Enter title, author, ISBN, or Barcode to search: ").strip().lower()
        results = [book for book in self.library if keyword in book.get("title", "").lower() or keyword in book.get("author", "").lower() or keyword in book.get("isbn", "").lower() or keyword in book.get("barcode", "").lower()]
        
        if results:
            print("\nSearch Results:")
            for book in results:
                self.display_book(book)
        else:
            print("No matching books found.\n")

    def display_all_books(self):
        """Display all books in the library."""
        if not self.library:
            print("Library is empty.\n")
            return
        print("\nYour Library:")
        for book in self.library:
            self.display_book(book)

    def display_book(self, book):
        """Display book details, handling missing fields gracefully."""
        read_status = "Read" if book.get("read", False) else "Unread"
        print(f"Title: {book.get('title', 'N/A')}, Author: {book.get('author', 'N/A')}, Year: {book.get('year', 'N/A')}, Genre: {book.get('genre', 'N/A')}, ISBN: {book.get('isbn', 'N/A')}, Barcode: {book.get('barcode', 'N/A')}, Status: {read_status}")
    
    def display_statistics(self):
        """Show statistics about the library."""
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book.get("read", False))
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        
        print("\nLibrary Statistics:")
        print(f"Total books: {total_books}")
        print(f"Read books: {read_books} ({percentage_read:.2f}% read)\n")
    
    def menu(self):
        """Display the menu and handle user input."""
        while True:
            print("\nPersonal Library Manager")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_all_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    manager.menu()
