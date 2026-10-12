class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        book.mark_as_borrowed()
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_available = True

    @property
    def is_available(self):
        return self._is_available

    def mark_as_borrowed(self):
        if not self._is_available:
            raise ValueError("Ce livre est déjà emprunté")
        self._is_available = False

class PrintedBook(Book):
    def __init__(self, title, author, isbn, number_of_pages):
        super().__init__(title, author, isbn)
        self.number_of_pages = number_of_pages

class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb

