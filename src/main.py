from datetime import datetime
from src.task import Task
from src.exceptions import TaskValidationError


def main():
    print("1. Создание задач")
    task1 = Task("T001", "Обработать заказ клиента #12345", priority=1)
    task2 = Task("T002", "Отправить уведомление пользователю", priority=3)
    task3 = Task("T003", "Обновить статистику базы данных", priority=5)

    print(f"   Создана: {task1}")
    print(f"   Создана: {task2}")
    print(f"   Создана: {task3}\n")

    print("2. Доступ к свойствам")
    print(f"   Задача1 создана: {task1.created_at}")
    print(f"   Возраст задачи1: {task1.age_seconds:.2f} сек")
    print(f"   Задача1 готова: {task1.is_ready}")
    print(f"   Задача3 готова: {task3.is_ready}\n")

    print("3. Проверка валидации")
    try:
        Task("", "Пустой ID", priority=1)
    except TaskValidationError as e:
        print(f"   Поймана ошибка: {e}")

    try:
        task1.priority = 10
    except TaskValidationError as e:
        print(f"   Поймана ошибка: {e}")

    try:
        task1.status = "invalid_status"
    except TaskValidationError as e:
        print(f"   Поймана ошибка: {e}\n")

    print("4. Проверка неизменяемости")
    try:
        task1.id = "T999"
    except AttributeError:
        print("   Поймана ошибка: Нельзя изменить ID")

    try:
        task1.created_at = datetime.now()
    except AttributeError:
        print("   Поймана ошибка: Нельзя изменить created_at\n")

    print("5. Изменение статуса задачи")
    print(f"   До: {task1}")
    task1.status = "in_progress"
    print(f"   После: {task1}")
    print(f"   Готова к выполнению: {task1.is_ready}\n")

    print("6. Изменение описания задачи")
    print(f"   Было: {task1.description}")
    task1.description = "Новое описание задачи"
    print(f"   Стало: {task1.description}\n")

    print("7. Вычисляемые свойства")
    import time
    time.sleep(1)
    print(f"   Возраст задачи1 через 1 секунду: {task1.age_seconds:.2f} сек")
    print(f"   is_ready: {task1.is_ready}\n")


if __name__ == "__main__":
    main()
