class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __str__(self):
        return '; '.join(self.items)

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def new_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        if task not in self.tasks[priority].items:
            self.tasks[priority].push(task)

    def remove_task(self, task):
        for stack in self.tasks.values():
            if task in stack.items:
                stack.items.remove(task)

    def __str__(self):
        sorted_priorities = sorted(self.tasks.keys())
        result = []
        for priority in sorted_priorities:
            result.append(f"{priority} — {self.tasks[priority]}")
        return '\n'.join(result)

# Пример использования
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)

print(manager)

# Удаление задачи
manager.remove_task("помыть посуду")
manager.remove_task("сдать ДЗ")
print("\nПосле удаления задачи 'помыть посуду' и 'сдать ДЗ':")
print(manager)
