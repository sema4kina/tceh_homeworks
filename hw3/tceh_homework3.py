#1 Random errors

import random

list1 = [ValueError, TypeError, RuntimeError]
def randomchoice(a):
	r_value = random.choice(a)
	if r_value == ValueError:
		raise ValueError
	elif r_value == TypeError:
		raise TypeError
	elif r_value == RuntimeError:
		raise RuntimeError
try:		
	randomchoice(list1)
except ValueError as answer:
	    print('Value error!!! ', answer)	
except TypeError as answer:
	    print('Type Error!!! ', answer)
except RuntimeError:
	    raise RuntimeError	

#2 type(element) and list.sort

import random
list1 = ['avb', 'sd', 23]
list2 = [1, 2, 7, 23, 0]

def list_process(l):
	try:
		for i in l:
			if type(i) == int:
				continue
		l.sort()
		print(l)
	except TypeError as answer:
		raise ValueError
        print('ValueError!')
	return l			
list_process(list2)		    	

#3 dict, keys - to string

dict1 = {1: 2, 23: 'fg', 46: 46, 'as': 23, 'jk':78}
def keys_process(d):
	for key, value in d.items():
		new_dict[str(key)] = value
	return new_dict			
new = keys_process(dict1)		

#4 Digits **

list1 = [1, 2, 6, 9, 12]
def multiply(l):
	m = 1
	for i in l:
		m = m * i
	return m	
print(multiply(list1))

#5 

list1 = [1, 2, 9, 4, 5,]
def handle_success():
	print('true')
def handle_error():
	raise ValueError()
	print('false')
def do_work(my_list,error_callback,success_callback):
	if my_list == sorted(my_list):
		success_callback()
	else:
		error_callback()	  	
do_work(list1, handle_error, handle_success)


         
