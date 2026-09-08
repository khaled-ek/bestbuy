from products import Product

class Store:
    def __init__(self, products_list):
        """
        Initialize a store with a list of products.

        Args:
            products_list (list[Product]): The initial list of products
                                            available in the store.
        """
        self.products_list = products_list
    def add_product(self, product):
        """
        Add a product to the store.

        Args:
            product (Product): The product to add to the store.
        """
        self.products_list.append(product)
    def remove_product(self, product):
        """
        Remove a product from the store.

        Args:
            product (Product): The product to remove from the store.
        """
        self.products_list.remove(product)
    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.

        Returns:
            int: The total number of product items currently in stock.
        """
        total = 0
        for product in self.products_list:
            total += product.get_quantity()
        return total
    def get_all_products(self) -> list[Product]:
        """
        Return all active products in the store.

        Returns:
            list[Product]: A list containing only the active products.
        """
        return [
            product
            for product in self.products_list
            if product.is_active()
        ]

    def order(self, shopping_list) -> float:
        """
        Process an order and calculate its total price.

        Quantities of identical products are combined before purchasing.
        This ensures that the total requested quantity of each product
        can be checked against the available stock.

        Args:
            shopping_list (list): A list of (product, quantity) tuples.

        Returns:
            float: The total price of the order.

        Raises:
            ValueError: If the total requested quantity of a product
                        exceeds its available quantity.
        """
        combined_order = {}

        for product, quantity in shopping_list:
            if product in combined_order:
                combined_order[product] += quantity
            else:
                combined_order[product] = quantity

        # Validate the complete order before changing any product quantities.
        for product, quantity in combined_order.items():
            if quantity > product.get_quantity():
                raise ValueError(
                    f'You ordered {quantity} from "{product.get_name()}". '
                    f'Only {product.get_quantity()} are available.'
                )

        total_price = 0

        for product, quantity in combined_order.items():
            total_price += product.buy(quantity)

        return total_price
