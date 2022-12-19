print('\ndel function')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
del books_list[0]
for i in range (0, len(books_list)):
    print(books_list[i])


print('\ndel function with list comprehension')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
del books_list[:]
for i in range (0, len(books_list)):
    print(books_list[i])

print('\ndel function with list comprehension start')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
del books_list[0:-2] #Start:End
for i in range (0, len(books_list)):
    print(books_list[i])

print('\ndel function with list comprehension step')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Gwoth Mindset']
del books_list[0::2] #Start:End:Step
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nMake a new list')
books_list = ['Seven habits', 'How to Influence People', 'First Things First', 'Grwoth Mindset']
new_books_list = books_list[:]
for i in range (0, len(books_list)):
    print(books_list[i])

print('\nMake a new list')
del books_list[:]
for i in range (0, len(new_books_list)):
    print(new_books_list[i])

print('\nMake a new list with comprehension: odd')
books_list = ['1 Seven habits', '2 How to Influence People', '3 First Things First', '4 Grwoth Mindset']
new_books_list = books_list[0::2]
for i in range (0, len(new_books_list)):
    print(new_books_list[i])

print('\nMake a new list with comprehension: even')
books_list = ['1 Seven habits', '2 How to Influence People', '3 First Things First', '4 Grwoth Mindset']
new_books_list = books_list[1::2]
for i in range (0, len(new_books_list)):
    print(new_books_list[i])

print('\nMake a new list with comprehension: even, minus variable')
books_list = ['1 Seven habits', '2 How to Influence People', '3 First Things First', '4 Grwoth Mindset']
new_books_list = books_list[0:-1:2]
for i in range (0, len(new_books_list)):
    print(new_books_list[i])

print('\nMake a new list with comprehension: odd')
books_list = ['1 Seven habits', '2 How to Influence People', '3 First Things First', '4 Grwoth Mindset']
print(books_list[0::2])






