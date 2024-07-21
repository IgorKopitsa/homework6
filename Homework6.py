my_dict={'Игорь' : 2013, 'Вера' : 2008 }
print(my_dict)
print(my_dict.get('Игорь'))
print(my_dict.get('Дима'))
my_dict={'Игорь' : 2013, 'Вера' : 2008 }
my_dict .update ({'Ирен' : 1980,
                  'Света' : 1999})
a= my_dict.pop("Игорь")
print(my_dict)

my_set= {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
print(my_set.update([8, 9]))
print(my_set.remove(3))
print(my_set)