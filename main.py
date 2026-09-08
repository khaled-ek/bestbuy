from products import Product
from store import Store
from colorama import Fore, Style


def list_store_products(store):
    """
    Display all products currently available in the store.

    Each product is displayed with its position in the product list
    and its product information.

    Args:
        store: The store containing the products to display.
    """
    products = store.get_all_products()
    print("------")
    for indx, prod in enumerate(products):
        print(str(indx+ 1) + ". " + prod.to_string())
    print("------")

def add_to_order_list(order_tuple_list, product, quantity):
    """
    Add a product and its requested quantity to the current order.

    Args:
        order_tuple_list (list): The list containing the order items.
        product: The product to add to the order.
        quantity (int): The requested quantity of the product.
    """
    order_tuple_list.append((product, quantity))

def get_order_data(store):
    """
    Collect product selections and quantities from the user.

    The user can repeatedly add products to the order by entering a
    product number and quantity. Entering an empty value ends the
    order-entry process.

    Args:
        store: The store containing the available products.

    Returns:
        list: A list of tuples containing the selected products and
                their requested quantities.
    """
    order_tuple_list = []
    while True:
        product_indx = input("Which product # do you want? ")
        quantity = input("What amount do you want?  ")

        if product_indx == "" or quantity == "":
            break

        if (
                product_indx.isdigit()
                and quantity.isdigit()
                and (int(product_indx) - 1) in range(len(store.products_list))
        ):
            add_to_order_list(order_tuple_list, store.get_all_products()[int(product_indx) - 1], int(quantity))
            print("Product added to list!")
            print()
        else:
            print("Error adding product!")
            print()
    return order_tuple_list


def start (store):
    """
    Start the store's command-line user interface.

    The menu allows the user to list products, display the total
    quantity of items in the store, create an order, or quit the
    application.

    Args:
        store: The store object used by the application.
    """
    while True:
        print ("    Store Menu")
        print ("    ----------")
        print ("1. List all products in store")
        print ("2. Show total amount in store")
        print ("3. Make an order")
        print ("4. Quit")
        choice = input("Please choose a number: ")
        if choice.isdigit():
            if choice == "1":
                list_store_products(store)
                print()
                #start(store)
            elif choice == "2":
                print("Total of " + str(store.get_total_quantity()) + " items in store")
                print()
                #start(store)
            elif choice == "3":
                try:
                    list_store_products(store)
                    print("When you want to finish order, enter empty text.")
                    order_tuple_list = get_order_data(store)
                    total_payment = store.order(order_tuple_list)
                    print("Order made! Total payment: $" + str(total_payment))
                    print()
                    #start(store)
                except ValueError as err:
                    print(Fore.RED + err.__str__() + Style.RESET_ALL)
            elif choice == "4":
                break
            else:
                print()
                #start(store)
        else:
            print ("Error with your choice! Try again!")
            print()
            #start(store)










try:
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
    best_buy = Store(product_list)

    start(best_buy)
except ValueError as error:
    print (error)
