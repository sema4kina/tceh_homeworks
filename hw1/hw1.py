questions_list = ['Какой язык мы изучаем?   ', 'При помощи какой функции можно определить тип данных?   ', 'Какой будет результат выполнения \n 13//4   ', 'Какой командой можно прервать цикл?   ', '"marathon"[3] = ', 'Сколько результатов выдаст программа: \n for count_id in range(0, 5): \n     print(count_id)   ', 'Каким будет конечное значение: \n for count_id in range(0, 1): \n     print(count_id)   ', 'Какая функция определяет длину строки?   ', 'Что будет результатом выполнения print(False and False)   -->  ', 'Ну и классический, кажется, вопрос. Как зовут нашего преподавателя?   ']
answers_list = ['python', 'type', '3', 'break', 'a', '5', '0', 'len', 'False', 'Никита']
count = 0
for question in questions_list:
    answer = input(question)
    if answer.lower() == answers_list[count].lower():
        print('Отлично')
        count += 1
    else:
        print('Будь внимательнее')
print('Молодец, твой результат за сегодня - {}'.format(count)) 