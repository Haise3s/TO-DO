from task import Task
from datetime import datetime

class TaskMeneger():
    def __init__(self, filename = "tasks.json"):
        self.filename = filename
        self.tasks = []
    
    def add_task(self, title, description = ""):
        self.tasks.append(Task(title, description))
    
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

    def complete_task(self,task_id):
        task = self.get_task(task_id)
        task.mark_completed()

a = TaskMeneger()
a.add_task("Гости", "Пойти в гости")
a.add_task("иду домой")
a.add_task("Командировка, уехать в командировку")
a.list_tasks()
print()
print()

#print(a.get_task(1))
#a.delete_task(1)
a.complete_task(3)
a.list_tasks()