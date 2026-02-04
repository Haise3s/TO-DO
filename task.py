from datetime import datetime

class Task:
    
    def __init__(self,task,description = '', status = 'Активно',id = None):
        self.id = id
        self.id = Task.task_count
        self.task = task
        self.description = description
        self.status = status
        self.created_at = datetime.now()

    def __str__(self):
        return f'Задача № {self.id}: {self.task}\nОписание: {self.description}, дата создания: {self.created_at.strftime("%d.%m.%Y %H:%M")} \nСтатуc выполнения: {self.status}\n'
    
    def __repr__(self):
        return f'Task(id = {self.id!r}, Задача = {self.task!r}, Описание = {self.description!r}, дата создания: {self.created_at} Статуc выполнения = {self.status!r})'
   
    def is_completed(self):
        return self.status == 'Выполнено'
    
    def mark_completed(self):
        if not self.is_completed():
            self.status = 'Выполнено'
        else:
            print("Задача уже выполнена")
    
    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
    @classmethod
    def from_dict(cls,data):
        task = cls(
            task = data ['task'],
            description = data.get('description',''),
            status  = data.get('status','Активно')
        )
        task.id = data['id']
        if data['id'] >= Task.task_count:
            Task.task_count = data['id'] + 1
        
        task.created_at =  datetime.fromisoformat(data['created_at'])
        return task
        