"""
Program perulangan membaca buku dengan while with undifined count
"""

books_count = 10
print('Mom said, "Please, read and understand all your books"')

books_read_count = 0
read_and_understood_count = 0
print(f"The number of books read and understand is {read_and_understood_count} books")

while books_read_count < books_count * 2:
    books_read_count = books_read_count + 1
    if read_and_understood_count == 9: # komputer membaca dari 0
        print(f"The order number {read_and_understood_count + 1} of the books is not understand yet")
        # Manusia membaca dari 1 (maka +1)
    else:
        read_and_understood_count = read_and_understood_count + 1
        print(f"The order of reading and understanding the book is {read_and_understood_count}")


if read_and_understood_count == books_count:
    print('Mom, All books can be read and understand')
else:
    print(f'Mom, I just can only read and understand {read_and_understood_count} books')
print(f'The number of books read and understand is {read_and_understood_count} books')
print("finish")