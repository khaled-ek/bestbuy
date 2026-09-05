class Product:
    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Product name cannot be empty")
        elif price < 0.0:
            raise ValueError("Product price cannot be negative")
        elif quantity < 0:
            raise ValueError("Product quantity cannot be negative")
        else:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

    def get_name(self):
        return self.name
    def get_price(self) -> float:
        return self.price
    def get_quantity(self) -> int:
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def is_active(self):
        return self.active
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
    def show(self):
        print(self.name, ", price: $", self.price, ", quantity: ", self.quantity)

    def to_string(self) -> str:
        return str(self.name) + ", price: $" + str(self.price) +  ", quantity: " + str (self.quantity)

    def buy(self, quantity) -> float :
        if quantity < 0:
            raise ValueError("Quantity must be greater than 0")
        elif quantity > self.quantity:
            raise ValueError("Only" + self.quantity + " are available, we cannot provide the requested quantity")
        else:
            self.quantity -= quantity
            return self.price * quantity

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

main()