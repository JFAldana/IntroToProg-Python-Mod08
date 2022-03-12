# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Joe Aldana,03.09.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JAldana, 9 March 2022 ,Modified code to complete assignment 8
    """

    # __ Constructor __
    def __init__(self, product_name, product_price):
        # -- Attributes--
        self.__product_name = product_name
        self.__product_price = product_price

    # __ Properties __
    # __ Product Name __
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, product_name):
        if str(product_name).isnumeric() == False:
            self.__product_name = product_name
        else:
            raise Exception("Please use letters only to name products!")

    # __ Product Price __
    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, product_price):
        if str(product_price).isalpha() == False:
            self.__product_price = product_price
        else:
            raise Exception("Please use just numbers for price!")

    def __str__(self):
        return self.product_name + ',' + self.product_price

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JAldana, 3 March 9,Modified code to complete assignment 8
    """

    # __ Read from File __
    @staticmethod
    def file_reader(file_name):
        file = open(file_name, 'r')
        for row in file:
            data = row.split(",")
            data_row = Product(data[0], data[1])
            lstOfProductObjects.append(data_row)
        file.close()
        return lstOfProductObjects

    # __ Write to File __
    @staticmethod
    def file_writer(file_name, lstOfProductObjects):
        file = open(file_name, 'w')
        for product in lstOfProductObjects:
            file.write(product.__str__() + '\n')
        file.close()

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ methods that run the I/O interface
    menu options (str)
    user input (str)
    show list (str)
    """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print(''' 
        Menu of Options 
         1) Add a new Product 
         2) Show current list of Product
         3) Save Data to File         
         4) Exit Program 
         ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] -")).strip()
        print()
        return choice

    @staticmethod
    def output_current_products_in_list(product_list):
        """ Shows the current products in the list
        """
        print("******* The current products are: *******")
        for row in product_list:
            print(row)
        print("*******************************************")
        print()

    @staticmethod
    def input_product_price():
        """  Gets product and price to be added to the list
        """
        user_product = str(input("What product to add? - ")).strip()
        user_price = str(input(f"What is {user_product.lower()}'s price ? - ")).strip()
        return user_product, user_price

# Main Body of Script  ---------------------------------------------------- #

FileProcessor.file_reader('products.txt')

while (True):
    IO.output_menu_tasks()
    choice_str = IO.input_menu_choice()

    if choice_str.strip() == '1':
        product, price = IO.input_product_price()
        new_product = Product(product, price)
        lstOfProductObjects.append(new_product.product_name + ',' + new_product.product_price + '\n')
        continue

    elif choice_str == '2':
        IO.output_current_products_in_list(lstOfProductObjects)
        continue

    elif choice_str == '3':  # Save Data to File
        FileProcessor.file_writer('products.txt', lstOfProductObjects)
        print("Data Saved!")
        continue

    elif choice_str == '4':
        print("Goodbye!")
        break
