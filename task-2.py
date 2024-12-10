import logging
from abc import ABC, abstractmethod
from typing import List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Принцип SRP
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип ISP
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def list_books(self) -> List[Book]:
        pass


# Принцип OCP
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < initial_count:
            logging.info(f"Book removed: {title}")
        else:
            logging.info(f"No book found with title: {title}")

    def list_books(self) -> List[Book]:
        return self.books


# Принцип DIP
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.list_books()
        if books:
            for book in books:
                logging.info(book)
        else:
            logging.info("Library is empty.")


# Принцип LSP
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logging.info("Exiting the program.")
                break
            case _:
                logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
