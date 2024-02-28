

phone_book=[]

fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	

with open('phone.txt','r',encoding='utf-8') as phb:

    for line in phb:

        record = dict(zip(fields, line.split(',')))
        #print(record)
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
	     
        phone_book.append(record)
    

    
#print(phone_book)


# def find_by_lastname(phone_book, last_name):
#     for i in phone_book:
#         for value in i.values():
#             if value == last_name:
#                 print(i)

# find_by_lastname(phone_book, 'Петров')

# def find_by_number(phone_book,number):
#     for i in phone_book:
#         for value in i.values():
#             if value == number:
#                 print(i)
            
            
# find_by_number(phone_book, '333')


# def change_number(phone_book,last_name,new_number):
#     for i in phone_book:
#         for value in i.values():
#             if value == last_name:
#                 i.pop('Телефон')
#                 i['Телефон'] = new_number

# change_number(phone_book, 'Иванов', 988)
# print(phone_book)

def delete_by_lastname(phone_book,lastname):
    for i in phone_book:
        for value in i.values():
            if value == lastname:
                phone_book.remove(i)

delete_by_lastname(phone_book, 'Васичкина')
print(phone_book)