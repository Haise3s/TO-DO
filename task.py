from datetime import datetime

class Task:
    
    def __init__(self,title,description = '', status = 'Активно', id = None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()

    def __str__(self):
        return f'Задача № {self.id}: {self.title}\nОписание: {self.description}, дата создания: {self.created_at.strftime("%d.%m.%Y %H:%M")} \nСтатуc выполнения: {self.status}\n'
    
    def __repr__(self):
        return f'Task(id = {self.id!r}, Задача = {self.title!r}, Описание = {self.description!r}, дата создания: {self.created_at} Статуc выполнения = {self.status!r})'
   
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
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
    @classmethod
    def from_dict(cls, data):
        task = cls(
            title = data['title'],
            description = data.get('description', ''),
            status = data.get('status', 'Активно'),
            id = data['id']
        )
        
        task.created_at = datetime.fromisoformat(data['created_at'])
        return task
