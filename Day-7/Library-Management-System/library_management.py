"""
=============================================================
  Library Management System (OOP + JSON Persistence)
  Day 7 Mini Project | MLB Python Bootcamp
=============================================================
  Demonstrates:
    - Classes & Objects (Book, Library)
    - Inheritance (DigitalBook extends Book)
    - Encapsulation (private attributes with controlled access)
    - JSON-based data persistence
    - Exception handling for invalid input
=============================================================
"""

import json
import os

DATA_FILE = "library_data.json"


# ─────────────────────────────────────────────
#  BOOK CLASS (Base Class)
# ─────────────────────────────────────────────

class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, genre,
                 total_copies, available_copies=None,
                 is_borrowed=False, borrowed_by=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        # If not provided, assume all copies are available
        self.available_copies = (
            available_copies if available_copies is not None else total_copies
        )
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by

    def display(self):
        status = "Available" if self.available_copies > 0 else "Out of Stock"
        print(f"  ID      : {self.book_id}")
        print(f"  Title   : {self.title}")
        print(f"  Author  : {self.author}")
        print(f"  Genre   : {self.genre}")
        print(f"  Copies  : {self.available_copies}/{self.total_copies} ({status})")
        if self.borrowed_by:
            print(f"  Last Borrower: {self.borrowed_by}")
        print("  " + "-" * 36)

    def borrow(self, borrower_name):
        if self.available_copies <= 0:
            print(f"  [Error] '{self.title}' has no available copies right now.")
            return False
        self.available_copies -= 1
        self.is_borrowed = True
        self.borrowed_by = borrower_name
        print(f"  ✅ '{self.title}' borrowed by {borrower_name}.")
        return True

    def return_book(self):
        if self.available_copies >= self.total_copies:
            print(f"  [Error] All copies of '{self.title}' are already in the library.")
            return False
        self.available_copies += 1
        if self.available_copies == self.total_copies:
            self.is_borrowed = False
        print(f"  ✅ '{self.title}' returned successfully.")
        return True

    def to_dict(self):
        """Convert the Book object into a JSON-serializable dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by,
        }


# ─────────────────────────────────────────────
#  DIGITAL BOOK CLASS (Inherits from Book)
#  Demonstrates inheritance + method overriding
# ─────────────────────────────────────────────

class DigitalBook(Book):
    """
    A digital/e-book is a special type of Book.
    Digital books have unlimited copies (no physical limit),
    so borrowing/returning logic is overridden.
    """

    def __init__(self, book_id, title, author, genre, file_size_mb):
        # Digital books have "unlimited" copies, represented as a large number
        super().__init__(book_id, title, author, genre,
                          total_copies=9999, available_copies=9999)
        self.file_size_mb = file_size_mb

    def display(self):
        super().display()
        print(f"  Format  : Digital (E-Book) | Size: {self.file_size_mb} MB")
        print("  " + "-" * 36)

    def borrow(self, borrower_name):
        # Overridden: digital books can always be "borrowed" (downloaded)
        print(f"  ✅ '{self.title}' (E-Book) downloaded by {borrower_name}.")
        self.borrowed_by = borrower_name
        return True

    def return_book(self):
        print(f"  ℹ️ '{self.title}' is a digital copy — no need to return it.")
        return True


# ─────────────────────────────────────────────
#  LIBRARY CLASS
# ─────────────────────────────────────────────

class Library:
    """Manages the full collection of books and handles persistence."""

    def __init__(self, name="My Library"):
        self.name = name
        self.books = []  # list of Book objects
        self.load_from_file()

    # ---------- Persistence ----------

    def load_from_file(self):
        if not os.path.exists(DATA_FILE):
            self.books = []
            return

        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            self.name = data.get("library_name", self.name)
            self.books = []
            for b in data.get("books", []):
                book = Book(
                    book_id=b["book_id"],
                    title=b["title"],
                    author=b["author"],
                    genre=b["genre"],
                    total_copies=b["total_copies"],
                    available_copies=b["available_copies"],
                    is_borrowed=b["is_borrowed"],
                    borrowed_by=b["borrowed_by"],
                )
                self.books.append(book)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"[Warning] Could not load data file properly: {e}")
            self.books = []

    def save_to_file(self):
        data = {
            "library_name": self.name,
            "total_books": len(self.books),
            "books": [book.to_dict() for book in self.books],
        }
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    # ---------- ID Generation ----------

    def generate_id(self):
        if not self.books:
            return "B001"
        last_num = max(int(b.book_id[1:]) for b in self.books)
        return f"B{str(last_num + 1).zfill(3)}"

    # ---------- Core Features ----------

    def add_book(self, title, author, genre, total_copies):
        book_id = self.generate_id()
        new_book = Book(book_id, title, author, genre, total_copies)
        self.books.append(new_book)
        self.save_to_file()
        print(f"  ✅ Book '{title}' added with ID: {book_id}")

    def view_all_books(self):
        if not self.books:
            print("\n  No books in the library yet.")
            return

        print(f"\n  === {self.name} — All Books ({len(self.books)}) ===")
        for book in self.books:
            book.display()

    def search_book(self, keyword):
        keyword = keyword.lower()
        results = [
            b for b in self.books
            if keyword in b.title.lower()
            or keyword in b.author.lower()
            or keyword == b.book_id.lower()
        ]

        if not results:
            print(f"  No books found matching '{keyword}'.")
        else:
            print(f"  Found {len(results)} result(s):")
            for book in results:
                book.display()

    def borrow_book(self, book_id, borrower_name):
        for book in self.books:
            if book.book_id == book_id:
                success = book.borrow(borrower_name)
                if success:
                    self.save_to_file()
                return
        print(f"  [Error] No book found with ID '{book_id}'.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                success = book.return_book()
                if success:
                    self.save_to_file()
                return
        print(f"  [Error] No book found with ID '{book_id}'.")


# ─────────────────────────────────────────────
#  INPUT HELPERS (Exception Handling)
# ─────────────────────────────────────────────

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [Error] This field cannot be empty.")


def input_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("  [Error] Please enter a number greater than 0.")
        except ValueError:
            print("  [Error] Please enter a valid whole number.")


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    print("\n" + "=" * 55)
    print("   📚 Library Management System")
    print("      OOP + JSON Persistence | Day 7 Project")
    print("=" * 55)

    library = Library("Python Community Library")
    print(f"\n  ✅ Loaded {len(library.books)} book(s) from '{DATA_FILE}'")

    while True:
        print("\n" + "-" * 40)
        print("  MENU")
        print("-" * 40)
        print("  1. Add New Book")
        print("  2. View All Books")
        print("  3. Search for a Book")
        print("  4. Borrow a Book")
        print("  5. Return a Book")
        print("  6. Exit")
        print("-" * 40)

        choice = input("  Enter choice (1-6): ").strip()

        try:
            if choice == "1":
                print("\n  ── Add New Book ──")
                title = input_non_empty("  Enter title: ")
                author = input_non_empty("  Enter author: ")
                genre = input_non_empty("  Enter genre: ")
                copies = input_positive_int("  Enter number of copies: ")
                library.add_book(title, author, genre, copies)

            elif choice == "2":
                library.view_all_books()

            elif choice == "3":
                keyword = input_non_empty("\n  Enter title, author, or book ID to search: ")
                library.search_book(keyword)

            elif choice == "4":
                book_id = input_non_empty("\n  Enter Book ID to borrow: ").upper()
                borrower = input_non_empty("  Enter your name: ")
                library.borrow_book(book_id, borrower)

            elif choice == "5":
                book_id = input_non_empty("\n  Enter Book ID to return: ").upper()
                library.return_book(book_id)

            elif choice == "6":
                print("\n  Goodbye! All records are saved. 👋\n")
                break

            else:
                print("  [Error] Invalid choice. Please enter a number from 1 to 6.")

        except Exception as e:
            # Catch-all safety net for unexpected errors
            print(f"  [Unexpected Error] {e}")


if __name__ == "__main__":
    main()
