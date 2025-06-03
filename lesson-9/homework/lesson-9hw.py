import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Пример использования:
c = Circle(5)
print("Площадь:", c.area())
print("Периметр:", c.perimeter())


from datetime import datetime

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")  # строка → дата

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

# Пример использования:
p = Person("Ali", "Uzbekistan", "2000-05-15")
print("Возраст:", p.get_age())



class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b

# Пример использования:
calc = Calculator()
print("Сложение:", calc.add(5, 3))
print("Деление:", calc.divide(10, 0))



import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

# Наследуем и реализуем конкретные формы:

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Формула Герона
        s = self.perimeter() 


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if node is None:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

# Пример:
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
print("Есть ли 15?", tree.search(15))  # True
print("Есть ли 7?", tree.search(7))    # False

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Стек пуст"
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

# Пример:
s = Stack()
s.push(10)
s.push(20)
print("Удалили:", s.pop())  # 20
print("Удалили:", s.pop())  # 10
print("Удалили:", s.pop())  # Стек пуст


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head  # вставляем в начало
        self.head = new_node

    def delete(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return "Элемент не найден"
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Пример:
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()          # 30 → 20 → 10 → None
ll.delete(20)
ll.display()          # 30 → 10 → None


class ShoppingCart:
    def __init__(self):
        self.items = {}  # словарь: товар → цена

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print("Товар не найден.")

    def total_price(self):
        return sum(self.items.values())

# Пример:
cart = ShoppingCart()
cart.add_item("Молоко", 12000)
cart.add_item("Хлеб", 6000)
print("Общая сумма:", cart.total_price())  # 18000
cart.remove_item("Хлеб")
print("После удаления:", cart.total_price())  # 12000

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "Стек пуст"
        return self.items.pop()

    def display(self):
        if not self.items:
            print("Стек пуст")
        else:
            print("Содержимое стека:", self.items)

# Пример:
s = Stack()
s.push(1)
s.push(2)
s.display()       # [1, 2]
print("Удалено:", s.pop())  # 2
s.display()       # [1]

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # добавляем в конец

    def dequeue(self):
        if self.is_empty():
            return "Очередь пуста"
        return self.items.pop(0)  # удаляем из начала

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Очередь:", self.items)

# Пример:
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.display()         # ['A', 'B']
print("Удалено:", q.dequeue())  # A
q.display()         # ['B']

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} пополнил счёт на {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств.")
        else:
            self.balance -= amount
            print(f"{self.name} снял {amount}")

    def get_balance(self):
        return self.balance

# Пример:
acc = BankAccount("Nora", 100000)
acc.deposit(50000)
acc.withdraw(20000)
print("Баланс:", acc.get_balance())  # 130000
































