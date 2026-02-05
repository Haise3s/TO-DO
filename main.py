from manager import TaskManager

def print_menu():
    print("\n" + "="*50)
    print("TODO LIST МЕНЕДЖЕР")
    print("="*50)
    print("1. 📋 Показать задачи")
    print("2. ➕ Добавить задачу")
    print("3. ✅ Отметить задачу как выполненную")
    print("4. ❌ Удалить задачу")
    print("5. 🔍 Найти задачу по ID")
    print("6. 💾 Сохранить задачи")
    print("7. 🚪 Выйти")
    print("="*50)

def show_tasks(manager):
    if not manager.tasks:
        print("📭 Список задач пуст.")
    else:
        print("1. Показать активные задачи")
        print("2. Показать выполненные задачи")
        print("3. Показать все задачи")
        choice = input("\nВыберите действие (1-3): ").strip()
        choice_dict = {'1':"\n===📊 АКТИВНЫЕ ЗАДАЧИ 📊===",
                        '2':"\n===✅ ВЫПОЛНЕНЫЕ ЗАДАЧИ ✅ ===",
                        '3':"\n=== ВСЕ ЗАДАЧИ ==="}
        print(choice_dict[choice])
        for task in manager.tasks:
            if choice == '1' and task.status == 'Активно': 
                status_icon =  "⏳"
                print(f"\n{task.id:3}. {status_icon} {task.title}")
                if task.description:
                    print(f"   📝 Описание: {task.description}")
                    print(f"   🕐 Создано: {task.created_at.strftime('%d.%m.%Y %H:%M')}")
                    print(f"   📊 Статус: {task.status}")
            elif choice == '2' and task.status == 'Выполнено':
                status_icon = "✅"
                print(f"\n{task.id:3}. {status_icon} {task.title}")
                if task.description:
                    print(f"   📝 Описание: {task.description}")
                    print(f"   🕐 Создано: {task.created_at.strftime('%d.%m.%Y %H:%M')}")
                    print(f"   📊 Статус: {task.status}")
            elif choice == '3':
                status_icon = "✅" if task.status == "Выполнено" else "⏳"
                print(f"\n{task.id:3}. {status_icon} {task.title}")
                if task.description:
                    print(f"   📝 Описание: {task.description}")
                    print(f"   🕐 Создано: {task.created_at.strftime('%d.%m.%Y %H:%M')}")
                    print(f"   📊 Статус: {task.status}") 

def show_tasks_for_delete(manager):
    if not manager.tasks:
        print("📭 Список задач пуст.")
    else:
        print("1. Удалить одну задачу задачу")
        print("2. Удалить все выполненные задачи")
        print("3. Удалить все задачи")
        choice = input("\nВыберите действие (1-3): ").strip()
        if choice == '1': 
            print("\n=== ВЫБЕРИТЕ ЗАДАЧУ ===")
            for task in manager.tasks:
                status_icon = "✅" if task.status == "Выполнено" else "⏳"
                print(f"{task.id:3}. {status_icon} {task.title}")
        return choice
    
def show_tasks_for_complete(manager):
    if not manager.tasks:
        print("📭 Список задач пуст.")
    else:
        print("\n=== ВЫБЕРИТЕ ЗАДАЧУ ===")
        for task in manager.tasks:
            if task.status == 'Активно': 
                status_icon = "⏳"
                print(f"{task.id:3}. {status_icon} {task.title}")

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
    show_tasks_for_complete(manager)
    try:
        task_id = int(input("\nВведите ID задачи для отметки: "))
        manager.complete_task(task_id)
        print(f"✅ Задача {task_id} отмечена как выполненная!")
    except ValueError:
        print("❌ Некорректный ID! Введите число.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def delete_task(manager):
    choise = show_tasks_for_delete(manager)
    if choise == '1':
        try:
            task_id = int(input("\nВведите ID задачи для удаления: "))
            manager.delete_task(task_id)
            print(f"✅ Задача {task_id} удалена!")
        except ValueError:
            print("❌ Некорректный ID!")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    if choise == '2':
        for task in  list(manager.tasks):
            if task.status == 'Выполнено':
                manager.delete_task(task.id)
        print(f"Все выполенные задачи были успешно удалены!✅")
    if choise == '3':
        for task in list(manager.tasks):
            manager.delete_task(task.id)
        print(f"Все задачи были успешно удалены!✅📝")

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
            show_tasks(manager)
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