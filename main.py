from products import Product
from store import Store
from colorama import Fore

def list_store_products(store):
    products = store.get_all_products()
    print("------")
    for indx in range(len(products)):
        print(str(indx+ 1) + ". " + products[indx].to_string())
    print("------")

def add_to_order_list(order_tuple_list, product, quantity):
    order_tuple_list.append((product, quantity))

def get_order_data(store, order_tuple_list):

    product_indx = input("Which product # do you want? ")
    quantity = input("What amount do you want?  ")
    if product_indx != "" and quantity != "":
        if product_indx.isdigit() and quantity.isdigit():
            if (int(product_indx) - 1) in range(len(store.products_list)):
                add_to_order_list(order_tuple_list, store.get_all_products()[int(product_indx) - 1], int(quantity))
                print("Product added to list!")
                print()
                get_order_data(store, order_tuple_list)
                return
            print("Error adding product!")
            print()
            get_order_data(store, order_tuple_list)



def start (store):
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
            start(store)
        elif choice == "2":
            print("Total of " + str(store.get_total_quantity()) + " items in store")
            print()
            start(store)
        elif choice == "3":
            try:
                order_tuple_list = []
                list_store_products(store)
                print("When you want to finish order, enter empty text.")
                get_order_data(store, order_tuple_list)
                total_payment = store.order(order_tuple_list)
                print("Order made! Total payment: $" + str(total_payment))
                print()
                start(store)
            except ValueError as err:
                print(Fore.RED + err.__str__())
        elif choice == "4":
            exit(0)
        else:
            print()
            start(store)
    else:
        print ("Error with your choice! Try again!")
        print()
        start(store)










try:
    product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
    best_buy = Store(product_list)

    start(best_buy)
except ValueError as error:
    print (error)