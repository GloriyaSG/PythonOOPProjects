from person.project import User
from typing import List, Dict

class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str:List[str]] = {}
        self.rented_books: Dict[str:Dict[str:int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            self.rented_books[user] = {book_name:days_to_return}



