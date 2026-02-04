from task import Task
import json
class TaskManager():
    def __init__(self, filename = "tasks.json", autoload = True, autosave = True):
        self.filename = filename
        self.next_id = 0
        self.tasks = []
        self.autosave = autosave
        if autoload:
            self.load_tasks() 
        
    def load_tasks(self):
        try:
            with open(self.filename, encoding = 'utf-8') as task_file:
                data = json.load(task_file)
            for task_dict in data:
                task = Task.from_dict(task_dict)
                self.tasks.append(task)
            if self.tasks:
                max_id = max(task.id for task in self.tasks)
                self.next_id = max_id
            else:
                self.next_id = 0
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден. Начинаем с пустого списка задач.")
            self.tasks = []
            self.next_id = 0
            
        except json.JSONDecodeError:
            print(f"Файл {self.filename} поврежден. Начинаем с пустого списка задач.")
            self.tasks = []
            self.next_id = 0

    def add_task(self, title, description = ""):
        self.next_id +=1
        self.tasks.append(Task(title, description, id = self.next_id))
        if self.autosave:
            self.save_tasks()
            
    def list_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print('Список задач пуст, добавьте задачу')
            return

    def get_task(self, task_id):
        for task in self.tasks:
            if task_id == task.id:
                return task
        raise ValueError(f"Задача с ID {task_id} не найдена")   
        
    def delete_task(self, task_id):
        task = self.get_task(task_id)
        self.tasks.remove(task)
        if self.autosave:
            self.save_tasks()

    def complete_task(self,task_id):
        task = self.get_task(task_id)
        task.mark_completed()
        if self.autosave:
            self.save_tasks()

    def save_tasks(self):
        try:
            task_data = [task.to_dict() for  task in self.tasks]
            with open(self.filename,'w',encoding = 'utf-8') as file_out:
                json.dump(task_data,file_out, ensure_ascii = False ,indent=2)
            print(f'Задачи сохранены успешно в {self.filename}')
            return True
        except PermissionError:
            print("Ошибка: нет прав для записи файла")
            return False
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            return False