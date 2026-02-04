from task import Task

class TaskManager():
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