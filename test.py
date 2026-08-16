import json
import datetime

def task_load():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        
    return tasks


def task_save(tasks_list):
    with open('tasks.json', 'w') as file:
            json.dump(tasks_list, file)


def add_task():
    new_id = 1
    title = input('Введите названия задачи: ')
    status = False
    date_create = datetime.datetime.now().strftime("%d.%m.%Y")

    tasks_list = task_load()
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
    task_save(tasks_list)
