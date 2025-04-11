class TodoList():
    def __init__(self):
        self.todo_list = []

    def add_task(self, task):
        self.todo_list.append(task)
        return self.todo_list

    def remove_task(self, task):
        self.todo_list.remove(task)
        return f"{task} was removed from your TO DO list"

