from food_order import calculate_total

def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
        
        # Calculate the total
        total = calculate_total(price, quantity)
        
        # Check if the returned total is a string (meaning it caught an error)
        if isinstance(total, str):
            print(total)
        else:
            print(f"Total Payment = RM {total:.2f}")
            
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()