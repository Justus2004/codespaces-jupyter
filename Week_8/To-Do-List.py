class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = 'Fertig' if self.completed else 'Nicht Fertig'
        return f'Titel: {self.title}\Beschreibung: {self.description}\nStatus: {status}\n'


class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        if self.items:
            for index, item in enumerate(self.items, 1):
                print(f"Element {index}:\n{item}")
        else:
            print("Keine Elemente in der To-Do-Liste.")

    def complete_item(self, index):
        if 1 <= index <= len(self.items):
            self.items[index - 1].complete()
            print(f"Element {index} als fertig markiert.")
        else:
            print("Nicht zugelassenes Element.")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Todo Item")
        print("2. Display Todo Items")
        print("3. Complete Todo Item")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter item title: ")
            description = input("Enter item description: ")
            item = TodoItem(title, description)
            todo_list.add_item(item)
            print("Todo item added successfully.")
        elif choice == '2':
            print("Todo Items:")
            todo_list.display_items()
        elif choice == '3':
            index = int(input("Enter index of item to mark as done: "))
            todo_list.complete_item(index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
