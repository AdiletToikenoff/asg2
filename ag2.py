# Interface for items
class Item:
    def __init__(self, title):
        self.title = title

    def display_info(self):
        raise NotImplementedError

# Interface for users
class User:
    def __init__(self, name):
        self.name = name

    def borrow_item(self, item):
        raise NotImplementedError

    def return_item(self, item):
        raise NotImplementedError

# Concrete implementation of a book item
class Book(Item):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display_info(self):
        print(f"Book: {self.title} by {self.author}")

# Concrete implementation of a librarian user
class Librarian(User):
    def add_item(self, item):
        # Logic to add item to catalog
        pass

    def remove_item(self, item):
        # Logic to remove item from catalog
        pass

# Concrete implementation of a patron user
class Patron(User):
    def borrow_item(self, item):
        # Logic to allow patron to borrow item
        pass

    def return_item(self, item):
        # Logic to allow patron to return item
        pass

# CLI for librarian interaction
class LibraryCLI:
    def __init__(self, librarian):
        self.librarian = librarian

    def add_item(self, item):
        self.librarian.add_item(item)

    def remove_item(self, item):
        self.librarian.remove_item(item)

# Usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
librarian = Librarian("John")
cli = LibraryCLI(librarian)
cli.add_item(book)
