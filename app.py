"""Prosta klasa do zarządzania listą zadań (CRUD)."""
class TodoList:
    def __init__(self):
        self.tasks = []

    """Dodaje nowe zadanie do listy."""
    def create(self, task: str) -> None:
        self.tasks.append(task)
        print(f"✔️ Zadanie '{task}' dodane.")

    """Odczytuje zapisane w liście"""
    def read(self) -> None:
        if not self.tasks:
            print("❌ Brak zadań.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"🎯 {i}. {task}")

    """Edytacja zapisanego zdania"""
    def edit(self, index: int, new_task: str) -> None:
        if 1 <= index <= len(self.tasks):
            old_task = self.tasks[index-1]
            self.tasks[index-1] = new_task
            print(f"✔️ Zadanie '{old_task}' zaktualizowane na '{new_task}'.")
        else:
            print("❌ Nieprawidłowy indeks.")

    """Usuwa zapisane zdanie"""
    def delete(self, index) -> None:
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index-1)
            print(f"✔️ Zadanie '{removed}' usunięte.")
        else:
            print("❌ Nieprawidłowy indeks.")

def main():
    todo = TodoList()
    while True:
        print("\n=== Lista Zadań (Todo) ===\n1. Dodaj zadanie\n2. Wyświetl zadania\n3. Edytuj zadanie\n4. Usuń zadanie\n5. Wyjdź\n")
        choice = input("Wybierz: ")
        if choice == '1':
            task = input("Nowe zadanie: ")
            todo.create(task)
        elif choice == '2':
            todo.read()
        elif choice == '3':
            index = int(input("Indeks do aktualizacji: "))
            new_task = input("Nowe zadanie: ")
            todo.edit(index, new_task)
        elif choice == '4':
            index = int(input("Indeks do usunięcia: "))
            todo.delete(index)
        elif choice == '5':
            break
        else:
            print("Zły wybór.")

if __name__ == "__main__":
    main()