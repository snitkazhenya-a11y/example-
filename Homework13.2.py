class Product:
    def __init__(self, name, price, description, size):
        self.name = name
        self.price = price
        self.description = description
        self.size = size
    def __str__(self):
        return f"{self.name} {self.price} {self.description} {self.size} грн"
class Customer:
    def __init__(self, last_name, first_name, middle_name, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_number = phone_number
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name} {self.phone_number}"
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}
    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    def total_price(self):
        total = 0
        for product, qty in self.items.items():
            total += product.price * qty
        return total
    def __str__(self):
        result = f"Замовлення для: {self.customer}\n"
        result += "Товар:\n"
        for product, qty in self.items.items():
            result += f"- {product.name} x {qty} = {product.price * qty} грн\n"
        result += f"Загальна сума: {self.total_price()} грн"
        return result
p1 = Product("Мишка", 500, "Ігрова", "10x10x5")
p2 = Product("Тримач", 1000, "Тримач для телефону", "15x7x3")
p3 = Product("Телефон", 3500, "Смартфон", "15x7x1")
p4 = Product("Навушники", 1500, "Навушники нові", "5x5x3")
customer = Customer("Снитка", "Євгеній", "Миколайович", "+380676310385")
order = Order(customer)
order.add_product(p3, 1)
order.add_product(p4, 2)
print(order)