import json
import datetime

def load_task():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        
    return tasks


def save_task(tasks_list):
    with open('tasks.json', 'w') as file:
            json.dump(tasks_list, file)


def add_task():
    new_id = 1
    title = input('Введите названия задачи: ')
    status = False
    date_create = datetime.datetime.now().strftime("%d.%m.%Y")

    tasks_list = load_task()
    task_id_list = []
    if tasks_list:
        for task in tasks_list:
            task_id_list.append(task['id'])
        new_id += max(task_id_list)

    new_task = {
        'id': new_id,
        'title': title,
        'status': status,
        'date_create': date_create,
    }

    tasks_list.append(new_task)
    save_task(tasks_list)

    

while True:
    print('''
1 Добавить задачу
2 Показать задачи
3 Просмотреть задачу
4 Изменить
5 Удалить
6 Завершить
7 Поиск
8 Фильтр
9 Сортировка
0 Выход''')
    
    user_choose = int(input('Выберете действие: '))

    if user_choose == 1:
        add_task()


    elif user_choose == 2:
        tasks_list = load_task()
        for task in tasks_list:
            print(f"{task['id']}: {task['title']}")


    elif user_choose == 3:
        id_task = int(input('Введите номер айди: '))

        tasks_list = load_task()
        for task in tasks_list:
            if task['id'] == id_task:
                print(f"{task['id']}: {task['title']}  --->  {task['status']}")
                break


    elif user_choose == 4:
        id_task = int(input('Введите номер айди: '))
        
        tasks_list = load_task()
        for task in tasks_list:
            if task['id'] == id_task:
                new_title = input('Введите новое название: ')
                task['title'] = new_title
                print(task['title'])
                save_task(tasks_list)
                break

    elif user_choose == 5:
        id_task = int(input('Введите номер айди: '))
        
        tasks_list = load_task()
        for task in tasks_list:
            if task['id'] == id_task:
                tasks_list.remove(task)
                save_task(tasks_list)
                break


    elif user_choose == 6:
        id_task = int(input('Введите номер айди: '))
        
        tasks_list = load_task()
        for task in tasks_list:
            if task['id'] == id_task:
                status_choose = int(input('Вы завершили проект?: \n1) Да \n2) Нет \n'))
                if status_choose == 1:
                    task['status'] = True
                elif status_choose == 2:
                    task['status'] = False
                save_task(tasks_list)
                break

    elif user_choose == 7:
        keyword = input('Введите название или ключевое слово: ').lower()

        tasks_list = load_task()

        for task in tasks_list:
            if keyword in task['title'].lower():
                print(task['title'])
            else:
                print('Такой задачи нет')

    elif user_choose == 8:
        tasks_list = load_task()

        print('''Фильтр по \n1) Статусу''')
        user_filter = int(input('Выберите фильтрацию: '))
        if user_filter == 1:
            status_filter = int(input('1) Выполненые 2) невыполненые \n'))
            if status_filter == 1:
                for task in tasks_list:
                    if task['status'] == True:
                        print(task['id'], task['title'], task['status'])
            if status_filter == 2:
                for task in tasks_list:
                    if task['status'] == False:
                        print(task['id'], task['title'], task['status'])    

    elif user_choose == 9:
        tasks_list = load_task()

        print('Сортировать по 1) названию')
        sorted_choose = int(input('Выберите действие: '))
        if sorted_choose == 1:
            tasks_list.sort(key=lambda task: task['title'])
        save_task(tasks_list)
    elif user_choose == 0:
        break


    print('\n-----------------------------')