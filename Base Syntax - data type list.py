books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
print('Show all variable od books_list')
print(books_list)

print('\nRun with "for in" method')
for book in books_list:
    print(book)

print('\nShow content of books list at certain indeks ')
print(books_list[0])
print(books_list[2])

print('\nShow content of books list with "for in" method')
for i in range (0, len(books_list)):
    print(books_list[i])

books_list = [1, 'Naruto Shippuden', -537, 3.14]
print('\nShow content of books list with "for in" method, which different type data for each element')
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nReturn initial value of books list')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
print('\nadd 1 new book')
books_list.append('Atomic Habbit')
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nClear list')
books_list.clear()
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nChange the first elemen')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
books_list[0] = 'Fairy Tale'
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nTake the second element')
taken_book = books_list.pop(1)
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nTaken book:')
print(taken_book)

print('\nPop') #take the last element
books_list.pop()
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nPop -4') #take the last element
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
books_list.pop(-4 )
for i in range (0, len(books_list)):
    print(books_list[i])

