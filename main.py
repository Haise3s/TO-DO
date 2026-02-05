from manager import TaskManager

def print_menu():
    print("\n" + "="*50)
    print("TODO LIST МЕНЕДЖЕР")
    print("="*50)
    print("1. 📋 Показать все задачи")
    print("2. ➕ Добавить задачу")
    print("3. ✅ Отметить задачу как выполненную")
    print("4. ❌ Удалить задачу")
    print("5. 🔍 Найти задачу по ID")
    print("6. 💾 Сохранить задачи")
    print("7. 🚪 Выйти")
    print("="*50)

def show_all_tasks(manager):
    print("\n=== ВСЕ ЗАДАЧИ ===")
    if not manager.tasks:
        print("📭 Список задач пуст.")
    else:
        for task in manager.tasks:
            status_icon = "✅" if task.status == "Выполнено" else "⏳"
            print(f"\n{task.id:3}. {status_icon} {task.title}")
            if task.description:
                print(f"   📝 Описание: {task.description}")
            print(f"   🕐 Создано: {task.created_at.strftime('%d.%m.%Y %H:%M')}")
            print(f"   📊 Статус: {task.status}")

def add_new_task(manager):
    print("\n=== ДОБАВЛЕНИЕ НОВОЙ ЗАДАЧИ ===")
    while True:
        title = input("Введите название задачи: ").strip()
        if title:
            break
        print("❌ Название не может быть пустым!")
    
    description = input("Введите описание (Enter чтобы пропустить): ").strip()
    
    try:
        task_id = manager.add_task(title, description)
        print(f"✅ Задача добавлена! ID: {task_id}")
    except Exception as e:
        print(f"❌ Ошибка при добавлении: {e}")

def complete_task(manager):
    show_all_tasks(manager)
    
    try:
        task_id = int(input("\nВведите ID задачи для отметки: "))
        manager.complete_task(task_id)
        print(f"✅ Задача {task_id} отмечена как выполненная!")
    except ValueError:
        print("❌ Некорректный ID! Введите число.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def delete_task(manager):
    show_all_tasks(manager)
    
    try:
        task_id = int(input("\nВведите ID задачи для удаления: "))
        manager.delete_task(task_id)
        print(f"✅ Задача {task_id} удалена!")
    except ValueError:
        print("❌ Некорректный ID!")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def find_task(manager):
    try:
        task_id = int(input("\nВведите ID задачи для поиска: "))
        task = manager.get_task(task_id)
        
        print(f"\n=== ЗАДАЧА #{task_id} ===")
        status_icon = "✅" if task.status == "Выполнено" else "⏳"
        print(f"{status_icon} {task.title}")
        if task.description:
            print(f"📝 Описание: {task.description}")
        print(f"🕐 Создано: {task.created_at.strftime('%d.%m.%Y %H:%M')}")
        print(f"📊 Статус: {task.status}")
        
    except ValueError:
        print("❌ Некорректный ID!")
    except Exception as e:
        print(f"❌ {e}")

def main():
    print("🚀 Загрузка TODO менеджера...")
    
    manager = TaskManager(filename="tasks.json", autoload=True, autosave=True)
    
    print(f"✅ Загружено задач: {len(manager.tasks)}")
    
    while True:
        print_menu()
        choice = input("\nВыберите действие (1-7): ").strip()
        
        if choice == "1":
            show_all_tasks(manager)
        elif choice == "2":
            add_new_task(manager)
        elif choice == "3":
            complete_task(manager)
        elif choice == "4":
            delete_task(manager)
        elif choice == "5":
            find_task(manager)
        elif choice == "6":
            if manager.save_tasks():
                print("✅ Задачи сохранены!")
        elif choice == "7":
            print("\n👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
        
        input("\n📝 Нажмите Enter чтобы продолжить...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа завершена пользователем.")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")