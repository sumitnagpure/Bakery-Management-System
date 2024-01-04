# Import the necessary libraries
import pandas as pd
from datetime import datetime

# Create an empty DataFrame for orders with an auto-incrementing Order ID
columns = ['Order_ID', 'Customer_Name', 'Order_Date', 'Food_Items', 'Quantities']
orders_df = pd.DataFrame(columns=columns)
order_id_counter = 1  # Initialize the counter for auto-incrementing Order ID

# Function to capture a new order with auto-generated Order ID
def capture_order():
    global order_id_counter  # Access the global counter variable
    order_id = order_id_counter
    order_id_counter += 1  # Increment the counter for the next order

    customer_name = input("Enter Customer Name: ")
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    food_items = input("Enter Food Items (comma-separated): ").split(',')
    quantities = input("Enter Quantities (comma-separated): ").split(',')
    
    order_data = {'Order_ID': order_id,
                  'Customer_Name': customer_name,
                  'Order_Date': order_date,
                  'Food_Items': food_items,
                  'Quantities': quantities}
    
    orders_df.loc[len(orders_df)] = order_data
    print("Order captured successfully!")

# Function to retrieve order based on Order ID
def retrieve_order(order_id):
    order = orders_df[orders_df['Order_ID'] == order_id]
    if not order.empty:
        print(order)
    else:
        print(f"No order found with Order ID {order_id}")

# Function to edit an existing order
def edit_order(order_id):
    global orders_df
    
    # Check if the order with the given Order ID exists
    if order_id not in orders_df['Order_ID'].values:
        print(f"No order found with Order ID {order_id}")
        return
    
    # Display the existing order for reference
    print("Existing Order:")
    print(orders_df[orders_df['Order_ID'] == order_id])
    
    # Capture the updated information
    customer_name = input("Enter Updated Customer Name (press Enter to keep the current value): ")
    food_items = input("Enter Updated Food Items (comma-separated, press Enter to keep the current value): ")
    quantities = input("Enter Updated Quantities (comma-separated, press Enter to keep the current value): ")
    
    # Update the order information
    orders_df.loc[orders_df['Order_ID'] == order_id, 'Customer_Name'] = customer_name if customer_name else orders_df.loc[orders_df['Order_ID'] == order_id, 'Customer_Name'].values[0]
    orders_df.loc[orders_df['Order_ID'] == order_id, 'Food_Items'] = food_items.split(',') if food_items else orders_df.loc[orders_df['Order_ID'] == order_id, 'Food_Items'].values[0]
    orders_df.loc[orders_df['Order_ID'] == order_id, 'Quantities'] = quantities.split(',') if quantities else orders_df.loc[orders_df['Order_ID'] == order_id, 'Quantities'].values[0]
    
    print("Order updated successfully!")

# Function to display the menu
def display_menu():
    print("\n===== Bakery Management System Menu =====")
    print("1. Capture New Order")
    print("2. Retrieve Order by Order ID")
    print("3. Edit Existing Order")
    print("4. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        capture_order()
    elif choice == '2':
        order_id_to_retrieve = int(input("Enter Order ID to retrieve: "))
        retrieve_order(order_id_to_retrieve)
    elif choice == '3':
        order_id_to_edit = int(input("Enter Order ID to edit: "))
        edit_order(order_id_to_edit)
    elif choice == '4':
        print("Exiting Bakery Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
