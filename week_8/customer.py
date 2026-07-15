def customer_data():
    name = input("Customer name : ")
    
    while True:
        Food_order = input("Food order (Cake/Muffin) : ").upper()
        if Food_order == "CAKE" or Food_order == "MUFFIN":
            break
        else: 
            print("#Note we just offer (Cake/Muffin).")
    Quantity = int(input("Quantity : "))
    delivery_Price = input(f"Price per Item (RM) : 3.00\nDelivery (Y/N) : ").upper()

    delivery_Price = 5.00 if delivery_Price == "Y" else 0
        

    return name,Food_order,Quantity,delivery_Price