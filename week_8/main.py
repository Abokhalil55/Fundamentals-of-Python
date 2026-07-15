from customer import customer_data
from receipt import customer_reciept

def main():
    name,Food_order,Quantity,delivery_Price = customer_data()
    customer_reciept(name,Food_order,Quantity,delivery_Price)

if __name__ =="__main__":
    main()