class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title} (Due: {self.due_date})\n  {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("❗ Неверный номер задачи.")


def main():
    todo = ToDoList()

    while True:
        print("\n===== Меню ToDo List =====")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать все задачи")
        print("4. Показать только невыполненные")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Название задачи: ")
            desc = input("Описание: ")
            due = input("Срок (например, 2025-06-01): ")
            task = Task(title, desc, due)
            todo.add_task(task)
        elif choice == "2":
            todo.list_tasks()
            idx = int(input("Введите номер задачи (с 0): "))
            todo.mark_task_complete(idx)
        elif choice == "3":
            todo.list_tasks()
        elif choice == "4":
            todo.list_incomplete_tasks()
        elif choice == "5":
            print("Выход.")
            break
        else:
            print("❗ Неверный выбор.")

if __name__ == "__main__":
    main()

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"📌 {self.title} — by {self.author}\n{self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for i, post in enumerate(self.posts):
            print(f"({i}) {post}")

    def posts_by_author(self, author_name):
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
        else:
            print("❗ Неверный индекс.")

    def edit_post(self, index, new_title=None, new_content=None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content
        else:
            print("❗ Неверный индекс.")

def main():
    blog = Blog()

    while True:
        print("\n===== Меню Блога =====")
        print("1. Добавить пост")
        print("2. Показать все посты")
        print("3. Показать посты по автору")
        print("4. Удалить пост")
        print("5. Редактировать пост")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Заголовок: ")
            content = input("Содержимое: ")
            author = input("Автор: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            name = input("Введите имя автора: ")
            blog.posts_by_author(name)

        elif choice == "4":
            blog.list_posts()
            idx = int(input("Введите номер поста для удаления: "))
            blog.delete_post(idx)

        elif choice == "5":
            blog.list_posts()
            idx = int(input("Введите номер поста для редактирования: "))
            new_title = input("Новый заголовок (оставь пустым, если не менять): ")
            new_content = input("Новое содержимое (оставь пустым, если не менять): ")
            blog.edit_post(idx, new_title or None, new_content or None)

        elif choice == "6":
            print("Выход из блога.")
            break

        else:
            print("❗ Неверный выбор.")


class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"💰 Пополнено: {amount}")
        else:
            print("❗ Сумма должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❗ Недостаточно средств.")
        elif amount > 0:
            self.balance -= amount
            print(f"💸 Снято: {amount}")
        else:
            print("❗ Неверная сумма.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Счёт: {self.acc_number}, Владелец: {self.holder_name}, Баланс: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_number] = acc

    def find_account(self, acc_number):
        return self.accounts.get(acc_number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print("✅ Перевод выполнен.")
            else:
                print("❗ Недостаточно средств.")
        else:
            print("❗ Один из счетов не найден.")

def main():
    bank = Bank()

    while True:
        print("\n===== Меню Банка =====")
        print("1. Добавить счёт")
        print("2. Пополнить счёт")
        print("3. Снять деньги")
        print("4. Проверить баланс")
        print("5. Перевести деньги")
        print("6. Показать детали счёта")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            num = input("Номер счёта: ")
            name = input("Имя владельца: ")
            bank.add_account(Account(num, name))

        elif choice == "2":
            num = input("Номер счёта: ")
            acc = bank.find_account(num)
            if acc:
                amount = float(input("Сумма пополнения: "))
                acc.deposit(amount)
            else:
                print("Счёт не найден.")

        elif choice == "3":
            num = input("Номер счёта: ")
            acc = bank.find_account(num)
            if acc:
                amount = float(input("Сумма снятия: "))
                acc.withdraw(amount)
            else:
                print("Счёт не найден.")

        elif choice == "4":
            num = input("Номер счёта: ")
            acc = bank.find_account(num)
            if acc:
                print(f"Баланс: {acc.get_balance()}")
            else:
                print("Счёт не найден.")

        elif choice == "5":
            from_acc = input("Счёт-отправитель: ")
            to_acc = input("Счёт-получатель: ")
            amount = float(input("Сумма перевода: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            num = input("Номер счёта: ")
            acc = bank.find_account(num)
            if acc:
                print(acc)
            else:
                print("Счёт не найден.")

        elif choice == "7":
            print("Выход из системы банка.")
            break

        else:
            print("❗ Неверный выбор.")

































