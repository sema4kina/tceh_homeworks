import random, collections

# How to make a list of str(odd) in the range from 0 to 100

list_of_odds = [str(i) for i in range(100) if i % 2 != 0]

# How to make a list of the non-iterable objects of another list

list_of_objects = [1, 'sadf', [sdf], None, 's']
new_list = [i for i in list_of_objects if isinstance(i, collections.Iterable)]

# How to make a list of tuples from a phrase 'The quick brown fox jumps over the lazy dog'

lazy_string = 'The quick brown fox jumps over the lazy dog'
# Превращаем строку в список элементов по разделителю

s = [(i.upper(), ''.join([random.choice([j.upper(), j.lower()]) for j in i]), len(i)) for i in lazy_string.split(' ')]
# Метод ''.join преобразует список в строку без разделителя (т.к. <<<<''>>>>.join)