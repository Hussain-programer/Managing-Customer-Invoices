# Managing-Customer-Invoices
Python program for managing customer invoices.
Program Enhancements
# Overview
This enhanced program manages customer invoices more efficiently by incorporating robust validation mechanisms, improved user interaction, and options for saving invoices in various formats. It aims to minimize errors and streamline the invoicing process.
# Input/Output Details
Inputs Required:
Customer Name: A string representing the customer's name.
Product Purchased: A string representing the product purchased.
Unit Price: A positive float representing the price per unit of the product.
Number of Units Purchased: A positive integer representing how many units were bought.
# Outputs Generated:
A detailed summary table displaying each customer's name, product purchased, total cost (including fees), and final amount due.
An option to save this information into a CSV file.
# Structure
The program consists of several modular components:
input_customer_data(): Collects and validates user inputs for multiple customers.
get_positive_float(prompt): Validates and retrieves a positive float from user input.
get_positive_int(prompt): Validates and retrieves a positive integer from user input.
calculate_total_cost(unit_price, number_of_units): Computes the total cost including fees.
display_invoice(customers): Outputs a formatted summary of all invoices.
save_to_file(customers, filename): Saves the invoice details to a CSV file.
main(): The entry point that orchestrates user interaction and calls other functions.
# User Guide
To run the program:
Execute the script in a Python environment.
Follow prompts to enter customer details. Type "exit" when done.
Review the displayed invoice summary.
Choose whether to save the invoice data to a file.
