# Name:Camille Dana
# ID:003277157
def nameOfBestCustomers(sales, customers, topN):
    """
    Returns the names of the top N customers with the largest sales.

    Args:
        sales (list of float): List of sales amounts.
        customers (list of str): List of customer names.
        topN (int): Number of top customers to display.

    Returns:
        list of str: Names of the top N customers.
    """
    # Create a list of tuples (customer_name, sale_amount)
    customer_sales = list(zip(customers, sales))

    # Sort the list in descending order based on sale_amount
    customer_sales.sort(key=lambda x: x[1], reverse=True)

    # Get the top N customers (or all if fewer than N)
    top_customers = customer_sales[:topN]

    # Display the results
    print(f"Top {topN} customers:")
    for i, (customer, sale) in enumerate(top_customers, start=1):
        print(f"{i}. {customer}: ${sale:.2f}")

    return [customer for customer, _ in top_customers]

if __name__ == "__main__":
    sales = []
    customers = []
    topN = int(input("Enter the number of top customers: "))
    while True:
        try:

            sale = float(input("Enter the purchase amount (or -1 to quit): "))

            if sale == -1:
                break
            customer = input("Enter the customer's name: ")
            sales.append(sale)
            customers.append(customer)
        except ValueError:
            print("Invalid input. Please enter a valid sale amount.")

    best_customers = nameOfBestCustomers(sales, customers, topN)
    #print(f"Best customers were: {', '.join(best_customers)}")
    print(f"Best customers were: {', '.join(best_customers)}")