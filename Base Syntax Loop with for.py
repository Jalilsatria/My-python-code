"""
Program perulangan membaca buku
"""

# Diketahui :
The_number_of_books = 10
print('Mom said, "Please, read all your books"')

The_number_of_books_read = 0
print(f"The number of books read is {The_number_of_books_read} books")

for The_number_of_books_read in range(1, The_number_of_books+1):
    print(f"The order of reading book is {The_number_of_books_read} ")

print(f'The_number_of_books_read is {The_number_of_books_read} books')


#Without "for"
print ('without "for"')
print("The order of reading book is 1")
print("The order of reading book is 2")
print("The order of reading book is 3")
print("The order of reading book is 4")
print("The order of reading book is 5")
print("The order of reading book is 6")
print("The order of reading book is 7")
print("The order of reading book is 8")
print("The order of reading book is 9")
print("The order of reading book is 10")