from app import TodoList

def test_create():
    todo = TodoList()
    todo.create("Testowe zadanie")
    assert len(todo.tasks) == 1
    assert todo.tasks[0] == "Testowe zadanie"

def test_update():
    todo = TodoList()
    todo.create("Stare zadanie")
    todo.update(1, "Nowe zadanie")
    assert todo.tasks[0] == "Nowe zadanie"

def test_delete():
    todo = TodoList()
    todo.create("Zadanie do usunięcia")
    todo.delete(1)
    assert len(todo.tasks) == 0