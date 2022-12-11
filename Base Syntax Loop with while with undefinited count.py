"""
Program perulangan membaca buku dengan while with undifined count
"""

The_number_of_books = 10
print('Mom said, "Please, read and understand all your books"')

The_count_of_read = 0
The_number_of_books_read_and_understand = 0
print(f"The number of books read and understand is {The_number_of_books_read_and_understand} books")

while The_count_of_read < The_number_of_books * 2:
    The_count_of_read = The_count_of_read + 1
    if The_number_of_books_read_and_understand == 9: # komputer membaca dari 0
        print(f"The order number {The_number_of_books_read_and_understand + 1} of the books is not understand yet")
        # Manusia membaca dari 1 (maka +1)
    else:
        The_number_of_books_read_and_understand = The_number_of_books_read_and_understand + 1
        print(f"The order of reading and understanding the book is {The_number_of_books_read_and_understand}")

if The_number_of_books_read_and_understand == The_number_of_books:
    print('Mom, All books can be read and understand')
else:
    print(f'Mom, I just can only read and understand {The_number_of_books_read_and_understand} books')
print(f'The number of books read and understand is {The_number_of_books_read_and_understand} books')
print("finish")