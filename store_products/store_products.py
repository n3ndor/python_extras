class Store:
    def __init__(self, name, list):
        self.name = name
        self.list = []

    def add_product(self, new_product):
        self.list.append(new_product)
        return self

    def sell_product(self, id):
        self.list[id].pop()
        return self


    def inflation(self, percent_increase):
        self.product.price *= self.percent_increase
        return self

    def set_clearance(self, category, percent_discount):
        for i in self.list:
            self.product.price *= self.percent_discount
            return self


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.is_increased = True | False
        self.percent_change = 1.1 # 10%

    def update_price(self, percent_change, is_increased):
        if self.is_increased == True:
            self.price = self.price * self.percent_change
        else:
            self.price = self.price * self.percent_change
        return self

    def print_info(self):
        print(f"Product Name: {self.name}, Category: {self.category}, Price: ${self.price}")
        
        return self


kiwi = Product("Kiwi", 20, "Fruit")
potato = Product("Potato", 5, "Vegetable")

kiwi.print_info()
kiwi.update_price(50, True).print_info()

potato.print_info()
potato.update_price(20, False).print_info()

a = Store("Fruit", "list_of_fruits")
b = Store("Vegetable", "list_of_vegetables")

a.add_product("kiwi")
b.add_product("potato")

print(a.name, a.list)
print(b.name, b.list)