import csv
import re

def input_customer_data():
    """Collects customer data from user input with validation."""
    customers = []
    while True:
        name = input("Enter customer name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        
        product = input("Enter product purchased: ")
        
        unit_price = get_positive_float("Enter unit price: ")
        number_of_units = get_positive_int("Enter number of units purchased: ")
        
        customers.append({
            'name': name,
            'product': product,
            'unit_price': unit_price,
            'number_of_units': number_of_units
        })
    
    return customers

def get_positive_float(prompt):
    """Prompts user for a positive float value with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be a positive number.")
            return value
        except ValueError as e:
            print(e)

def get_positive_int(prompt):
    """Prompts user for a positive integer value with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be a positive integer.")
            return value
        except ValueError as e:
            print(e)

def calculate_total_cost(unit_price, number_of_units):
    """Calculates total cost including a 10% fee."""
    subtotal = unit_price * number_of_units
    total_cost = subtotal + (subtotal * 0.10)  # Adding 10% fee
    return total_cost

def display_invoice(customers):
    """Displays a formatted invoice for all customers."""
    print("\nCustomer Invoice Summary")
    print("-" * 60)
    print(f"{'Customer Name':<25}{'Product':<25}{'Total Cost (£)':<20}{'Final Amount (£)':<20}")
    print("-" * 60)
    
    for customer in customers:
        total_cost = calculate_total_cost(customer['unit_price'], customer['number_of_units'])
        print(f"{customer['name']:<25}{customer['product']:<25}{total_cost:<20.2f}{total_cost:<20.2f}")
    
def save_to_file(customers, filename='invoices.csv'):
    """Saves customer data to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Customer Name', 'Product', 'Unit Price', 'Number of Units', 'Total Cost (£)', 'Final Amount (£)'])
        
        for customer in customers:
            total_cost = calculate_total_cost(customer['unit_price'], customer['number_of_units'])
            writer.writerow([customer['name'], customer['product'], customer['unit_price'], 
                             customer['number_of_units'], total_cost, total_cost])

def main():
    """Main function to run the program."""
    customers = input_customer_data()
    
    if customers:
        display_invoice(customers)
        
        save_choice = input("Do you want to save the invoice to a file? (yes/no): ")
        if save_choice.lower() == 'yes':
            filename = input("Enter filename (default is invoices.csv): ") or 'invoices.csv'
            save_to_file(customers, filename)
            print(f"Invoices saved to {filename}.")
    
if __name__ == "__main__":
    main()
