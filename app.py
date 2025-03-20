import streamlit as st
import json
import base64
import logging

def set_background(image_file):
    """Set background image."""
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

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

    def add_book(self, title, author, year, genre, isbn, barcode, read_status):
        """Add a new book to the library."""
        book = {"title": title, "author": author, "year": year, "genre": genre, "isbn": isbn, "barcode": barcode, "read": read_status}
        self.library.append(book)
        self.save_library()

    def remove_book(self, title):
        """Remove a book from the library by title."""
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        self.save_library()

    def search_books(self, keyword):
        """Search for a book by title, author, genre, ISBN, or Barcode."""
        return [book for book in self.library if keyword.lower() in book.get("title", "").lower() or keyword.lower() in book.get("author", "").lower() or keyword.lower() in book.get("genre", "").lower() or keyword.lower() in book.get("isbn", "").lower() or keyword.lower() in book.get("barcode", "").lower()]

    def get_statistics(self):
        """Show statistics about the library."""
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book.get("read", False))
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        return total_books, read_books, percentage_read

# Streamlit UI
st.set_page_config(layout="wide", page_title="Personal Library Manager")
st.title("📚 Personal Library Manager")
manager = PersonalLibraryManager()

# Sidebar with developer info and version history
with st.sidebar:
    st.header("ℹ️ Developer Info")
    st.write("**Developer :** Fahad Khakwani")
    st.write("**LinkedIn :** [Profile](https://www.linkedin.com/in/fahad-khakwani-3aa655265/)")
    st.write("**Contact :** [Email](fahadyousufkhakwani@gmail.com)")
    st.write("**Mobile :** [Whatsapp](+92-312-9092620)")
    
    st.header("📜 About Versions")
    st.write("- **Version 1.0 :** [CLI_GitHub](https://github.com/Fahad-FullStackDeveloper/personal-library)")
    st.write("- **Version 2.1 :** [Streamlit](https://fahad-fullstackdeveloper-personal-library-app-aeaauq.streamlit.app/)")

# Add Book
set_background("background.jpg")
with st.expander("➕ Add a Book"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=2100, step=1)
    genre = st.text_input("Genre")
    isbn = st.text_input("ISBN")
    barcode = st.text_input("Barcode")
    read_status = st.checkbox("Read")
    if st.button("Add Book"):
        manager.add_book(title, author, year, genre, isbn, barcode, read_status)
        st.success("Book added successfully!")
        st.experimental_rerun()

# Remove Book
with st.expander("❌ Remove a Book"):
    book_to_remove = st.text_input("Enter book title to remove")
    if st.button("Remove Book"):
        manager.remove_book(book_to_remove)
        st.success("Book removed successfully!")
        st.experimental_rerun()

# Search Book
with st.expander("🔍 Search for a Book"):
    search_keyword = st.text_input("Enter title, author, genre, ISBN, or Barcode")
    if search_keyword:
        results = manager.search_books(search_keyword)
        if results:
            st.write("### Search Results:")
            st.table(results)
        else:
            st.warning("No matching books found.")

# Display All Books in Wide Table View
st.write("### 📖 View Library")
if manager.library:
    st.dataframe(manager.library, use_container_width=True)
else:
    st.warning("Library is empty.")

# Display Statistics
with st.expander("📊 Library Statistics"):
    total_books, read_books, percentage_read = manager.get_statistics()
    st.write(f"Total books: {total_books}")
    st.write(f"Read books: {read_books} ({percentage_read:.2f}% read)")
