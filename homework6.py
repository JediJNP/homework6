#Словарь
my_dict = {'Anna' : 1997 , 'Irina' : 1998 , 'Egor' : 1999}
print('мой "словарь":' , my_dict)
print('значение по существующему ключу:' , my_dict['Irina'])
print('значение по отсутствующему ключу без ошибки:' , my_dict.get('Ignat'))
my_dict.update({'Alex' : 1987 , 'Kate' : 2001})
print('добавлены 2 пары:' , my_dict)
deleted = my_dict.pop('Egor')
print('значение удаленной пары:' , deleted)
print('сейчас словарь выглядит так:' , my_dict)

#Множество
my_set = {11, 7 , True , 7 , 'dictionary' , True , 8.7 , 'dictionary'}
print('моё "множество:"' , my_set)
my_set.add('новый элемент' )
my_set.add((15 , 47, 24))
print('добавлено 2 элемента:"' , my_set)
my_set.remove(11)
print('удален 1 элемент:"' , my_set)