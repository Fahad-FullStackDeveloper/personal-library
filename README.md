# Personal Library Manager

## Overview
The **Personal Library Manager** is a simple command-line application that allows users to manage their book collection efficiently. It provides features to add, remove, search, display books, and track reading status. The library data is stored in a JSON file to persist book details between sessions.

## Features
- **Add a Book:** Users can add books with details like title, author, publication year, genre, ISBN, barcode, and read status.
- **Remove a Book:** Books can be removed from the collection by title.
- **Search for a Book:** Search by title, author, ISBN, or barcode.
- **Display All Books:** View all books stored in the library.
- **Display Statistics:** Shows total books and the percentage of books read.
- **Data Persistence:** Book details are stored in a JSON file (`library.json`).

## Installation & Usage
### Requirements
- Python 3.x

### How to Run
1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Run the script:
   ```sh
   python lib.py
   ```
4. Use the menu system to interact with the library.

## Menu Options
```
Personal Library Manager
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
```
Select an option by entering the corresponding number.

## Data Storage
All book records are stored in `library.json` in the following format:
```json
[
    {
        "title": "Book Title",
        "author": "Author Name",
        "year": 2024,
        "genre": "Fiction",
        "isbn": "1234567890",
        "barcode": "987654321",
        "read": true
    }
]
```

## Contributions
Feel free to fork and improve this project by adding more features like:
- Sorting books
- Exporting data to CSV
- GUI version

## GitHub Repository
Find the source code on GitHub: [GitHub Repository](https://github.com/yourusername/personal-library-manager)

## License
This project is open-source. Use and modify as needed.

