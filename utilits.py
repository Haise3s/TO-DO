def print_task_card(task):
    status_icon = "✅" if task.status == "Выполнено" else "⏳"
    print(f"\n{task.id:3}. {status_icon} {task.title}")
    if task.description:
        print(f"   📝 Описание: {task.description}")
        print(f"   🕐 Создано: {task.created_at.strftime('%d.%m.%Y %H:%M')}")
        print(f"   📊 Статус: {task.status}")

    