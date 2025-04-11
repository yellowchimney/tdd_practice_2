from lib.todo_list import TodoList

def test_adds_task_to_list():
    todo = TodoList()
    result = todo.add_task("help")

    assert result == ["help"]

def test_adds_multiple_tasks_to_list():
    todo = TodoList()
    todo.add_task("HELP!")
    todo.add_task("Help!")
    result = todo.add_task("help")

    assert result == ["HELP!", "Help!", "help"]

def test_removes_given_task_from_list():
    todo = TodoList()
    todo.add_task("HELP!")
    todo.add_task("Help!")
    todo.add_task("help")
    result = todo.remove_task("Help!")

    assert todo.todo_list == ["HELP!", "help"]
    assert result == "Help! was removed from your TO DO list"