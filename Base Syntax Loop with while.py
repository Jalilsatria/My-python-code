"""
Program perulangan membaca buku dengan while
"""

The_number_of_books = 10
print('Mom said, "Please, read all your books"')

The_number_of_books_read = 0
print(f"The number of books read is {The_number_of_books_read} books")

while The_number_of_books_read < The_number_of_books:
    The_number_of_books_read = The_number_of_books_read + 1
    print(f"The order of reading book is {The_number_of_books_read}")

print(f'The_number_of_books_read is {The_number_of_books_read} books')