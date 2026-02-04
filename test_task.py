from task import Task
import unittest

class TestTask(unittest.TestCase):
    def test_create_basic(self):
        title = "Название задачи"
        desc = "Описание задачи"

        task = Task(title,desc)
        self.assertEqual(task.task, title)
        self.assertEqual(task.description, desc)
        self.assertEqual(task.status, "Активно")
        self.assertIsInstance(task.created_at, datetime)
        print("✓ test_create_task_basic успешно пройден")

    def test_mark_completed(self):
        task = Task('Тест')
        task.mark_completed()
        self.assertEqual(task.status, "Выполнено")
        self.assertTrue(task.is_completed())
        print("✓ test_mark_completed успешно пройден")
    
    def test_to_dict(self):
        task = Task('Тесты', 'Описание')
        result = task.to_dict()
        expected_keys = ['id','task','description','status','created_at'] 
        for key in expected_keys:
            self.assertIn(key, result)

        self.assertIsInstance(result['created_at'], str)
        self.assertIn('T', result['created_at'])
        print("✓ test_to_dict пройден")
    
if __name__ == '__main__':
    unittest.main()