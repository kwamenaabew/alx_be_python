# library_management.py

class Book:
    """
    Represents a book in the library.
    Public attributes:
      - title: the book’s title
      - author: the book’s author
    Private attribute:
      - _is_checked_out: True if the book is currently checked out
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark the book as checked out.
        Returns True if successful, False if it was already checked out.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """
        Mark the book as returned (available).
        Returns True if successful, False if it was not checked out.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is not currently checked out."""
        return not self._is_checked_out


class Library:
    """
    Represents a simple library managing a collection of Book instances.
    Private attribute:
      - _books: list of Book objects in the library
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """
        Add a Book instance to the library’s collection.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Attempt to check out the book with the given title.
        Prints a message if the book isn’t found or already checked out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"No book with title '{title}' found.")
        return False

    def return_book(self, title):
        """
        Attempt to return the book with the given title.
        Prints a message if the book isn’t found or wasn’t checked out.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"No book with title '{title}' found.")
        return False

    def list_available_books(self):
        """
        Print all books that are not currently checked out,
        one per line in the format: Title by Author
        """
        available = [b for b in self._books if b.is_available()]
        if not available:
            print("No books currently available.")
            return
        for b in available:
            print(f"{b.title} by {b.author}")
