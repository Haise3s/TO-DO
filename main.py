from manager import TaskManager  # берём наш менеджер задач

def main():
    print("🚀 Запуск менеджера задач...")
    manager = TaskManager()
    
    manager.run()
    
    print("👋 Выход из программы")

if __name__ == "__main__":
    main()