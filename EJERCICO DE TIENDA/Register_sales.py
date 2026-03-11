
def register_sales():

    sales = []
    validation = True

    while validation:
        try: 
            
            product = input("Product name: ")
            price = float(input("Unit price: "))
            quantity = int(input("Quantity: "))

            sale = {
                "product": product,
                "price": price,
                "quantity": quantity
            }

            sales.append(sale)

            option = input("Register another sale? (yes/no): ").lower()

            if option == "no":
                validation = False
                return sales
        except ValueError:
            print("Invalid input. Please enter valid numbers for price and quantity.")
            
            