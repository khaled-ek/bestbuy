class Product:

    def __init__(self, name, price, quantity):
        """
        Initialize a new product with a name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of one product.
            quantity (int): The number of items available in stock.

        Raises:
            ValueError: If the product name is empty.
            ValueError: If the price is negative.
            ValueError: If the quantity is negative.
        """
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
            if self.quantity == 0:
                self.active = False
            else:
                self.active = True

    def get_name(self):
        """
        Returns:
            str: The product name.
        """
        return self.name
    def get_price(self) -> float:
        """
        Returns:
            float: The product price.
        """
        return self.price
    def get_quantity(self) -> int:
        """
        Returns:
            int: The available product quantity.
        """
        return self.quantity
    def set_quantity(self, quantity):
        """
        Set a new quantity for the product.

        The quantity cannot be negative. If the new quantity is zero,
        the product is automatically deactivated.

        Args:
            quantity (int): The new quantity of the product.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")
        else:
            self.quantity = quantity
            if self.quantity == 0: self.deactivate()
    def is_active(self):
        """
        Check whether the product is currently active.

        Returns:
            bool: True if the product is active, otherwise False.
        """
        return self.active
    def activate(self):
        """
        Activate the product.
        """
        self.active = True
    def deactivate(self):
        """
        Deactivate the product.
        """
        self.active = False
    #def show(self):
    #    print(self.name, ", price: $", self.price, ", quantity: ", self.quantity)

    def to_string(self) -> str:
        """
        Return the product information as a formatted string.

        Returns:
            str: A string containing the product name, price, and quantity.
        """
        return str(self.name) + ", price: $" + str(self.price) +  ", quantity: " + str (self.quantity)

    def buy(self, quantity) -> float :
        """
            Purchase a specified quantity of the product.

            The method checks whether the product is active and whether the
            requested quantity is valid and available. If the purchase is
            successful, the stock quantity is reduced and the total price
            of the purchase is returned.

            Args:
                quantity (int): Number of items to purchase.

            Returns:
                float: Total price of the purchased items.
                       Returns 0 if the product is inactive.

            Raises:
                ValueError: If quantity is less than or equal to zero.
                ValueError: If the requested quantity exceeds the available stock.
        """

        if self.is_active():
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")
            elif quantity > self.quantity:
                raise ValueError("You ordered " + str(quantity) + " from the \"" + self.name + "\" Only " + str(self.quantity) + " are available, we cannot provide the requested quantity")
            else:
                self.quantity -= quantity
                if self.quantity == 0: self.deactivate()
                return self.price * quantity
        return 0
