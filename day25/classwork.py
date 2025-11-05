integers = [1,2,3,4,5,6,7,8,9,10]

def square(num: int) -> int:
    return num * num

integers_squared = list(map(square, integers))

def is_even(num: int) -> bool:
    return num % 2 == 0

def all_even(nums: list) -> list:
    """returns list with only its even numbers"""
    return list(filter(is_even, nums))

def capitalize_all(strings: list) -> list:
    return list(map(lambda s: s.upper(), strings))

test_strings = ["hello", "world", "python", "rocks"]

def string_lengths(strings: list) -> list:
    return list(map(lambda s: len(s), strings))

sample_strings = ["apple", "banana", "kiwi", "strawberry", "fig"]
print(string_lengths(sample_strings))

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

def long_books(books: list[Book]) -> list[str]:
    """Return the titles of books that have more than 300 pages."""
    result = []
    for book in books:
        if book.pages > 300:
            result = result + [book.title]
    return result

books = [
    Book(title="War and Peace", author="Leo Tolstoy", pages=1225),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald", pages=180),
    Book(title="Moby Dick", author="Herman Melville", pages=635),
    Book(title="Animal Farm", author="George Orwell", pages=112),
    Book(title="Don Quixote", author="Miguel de Cervantes", pages=863)
]
print(long_books(books))

def filter_by_author(books: list, author: str) -> list:
    result = []
    for book in books:
        if book.author == author:
            result.append(book.title)
    return result

print(filter_by_author(books, "George Orwell"))

# print(capitalize_all(test_strings))
# print(all_even(integers))
# print(integers_squared)
