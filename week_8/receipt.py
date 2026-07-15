def customer_reciept(name,Food_order,Quantity,delivery_Price):
    subtotal = Quantity * 3
    service_charge = subtotal * 0.05
    grand_total = subtotal + service_charge + delivery_Price
    
    print("\n========== RECEIPT ==========")
    print(f"Customer : {name}")
    print(f"Food     : {Food_order}")
    print(f"Quantity : {Quantity}")
    print("Price    : RM 3.00")
    
    print("----------------------------")
    print(f"Subtotal : RM {subtotal:.2f}")
    print(f"Service Charge (5%) : RM {service_charge:.2f}")
    print(f"Delivery Charge : RM {delivery_Price}")
    
    print("----------------------------")
    print(f"TOTAL    : RM {grand_total:.2f}")
    print("=============================")