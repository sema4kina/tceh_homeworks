list1 = [1, 2, 9, 4, 5,]
def handle_success():
	print('true')
def handle_error():
	raise ValueError()
	print('false')
def success_callback():
	pass
def error_callback():
	pass
def do_work(my_list,error_callback,success_callback):
	if my_list == sorted(my_list):
		success_callback()
		handle_success()
	else:
		handle_error()
		error_callback()	  	
do_work(list1, error_callback, success_callback)