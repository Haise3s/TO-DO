from manager import TaskManager
import unittest

class TestTaskMeneger(unittest.TestCase):
   
    def setUp(self):
        self.manager = TaskManager()
    
    def test_initial_state(self):
        self.assertEqual(len(self.manager.tasks), 0)
        print("✓ test_initial_state пройден")
    
    def test_add_task(self):
        initial_count = len(self.manager.tasks)
        self.manager.add_task("Тестовая задача", "Описание")
        
        self.assertEqual(len(self.manager.tasks), initial_count + 1)
        self.assertEqual(self.manager.tasks[-1].title, "Тестовая задача")
        print("✓ test_add_task пройден")
    
    def test_add_multiple_tasks(self):
        self.manager.add_task("Задача 1")
        self.manager.add_task("Задача 2")
        
        self.assertEqual(len(self.manager.tasks), 2)
        self.assertEqual(self.manager.tasks[0].id, 1)
        self.assertEqual(self.manager.tasks[1].id, 2)
        print("✓ test_add_multiple_tasks пройден")
    
    def test_get_task_success(self):
        self.manager.add_task("Найти меня")
        task = self.manager.get_task(1)
        
        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Найти меня")
        print("✓ test_get_task_success пройден")
    
    def test_get_task_not_found(self):
        self.manager.add_task("Задача")
        
        with self.assertRaises(ValueError) as context:
            self.manager.get_task(999)
        
        self.assertIn("не найдена", str(context.exception))
        print("✓ test_get_task_not_found пройден")
    
    def test_delete_task(self):
        self.manager.add_task("Удалить меня")
        self.manager.add_task("Остаться")
        
        initial_count = len(self.manager.tasks)
        self.manager.delete_task(1)
        
        self.assertEqual(len(self.manager.tasks), initial_count - 1)
        
        with self.assertRaises(ValueError):
            self.manager.get_task(1)  
        
        task2 = self.manager.get_task(2)
        self.assertEqual(task2.title, "Остаться")
        print("✓ test_delete_task пройден")
    
    def test_complete_task(self):
        self.manager.add_task("Выполнить меня")
        
        task = self.manager.get_task(1)
        self.assertEqual(task.status, "Активно")
        
        self.manager.complete_task(1)
        
        task = self.manager.get_task(1)
        self.assertEqual(task.status, "Выполнено")
        print("✓ test_complete_task пройден")
    
    def test_list_tasks_empty(self):
        import io
        import sys
        
        captured = io.StringIO()
        sys.stdout = captured
        
        self.manager.list_tasks()
        
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        
        self.assertIn('добавьте задачу', output)
        print("✓ test_list_tasks_empty пройден")

    def test_list_tasks_with_content(self):
        """Тест: list_tasks() выводит задачи при непустом списке"""
        self.manager.add_task("Купить молоко")
        self.manager.add_task("Сделать ДЗ")
        
        import io
        import sys
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        self.manager.list_tasks()
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Купить молоко", output)
        self.assertIn("Сделать ДЗ", output)
        
        print("✓ test_list_tasks_with_content пройден")

if __name__ == '__main__':
    unittest.main()
