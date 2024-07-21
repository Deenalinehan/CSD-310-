import mysql.connector

config = {
    'user': 'root',
    'password': input("Provide your root password: "), 
    'host': '127.0.0.1',
    'database': 'bacchus_winery'  
}
# This functions will call every table and its contents to be displayed in the console.
def displayAllTableData():
    # Display contents of department Table
    cursor.execute("SELECT * FROM department")
    departments = cursor.fetchall()
    print("-- DISPLAYING Department RECORDS --")
    for department in departments:
        print("Department ID: {}\nDepartment Name: {}\nDepartment Leader: {}\nTotal Employees: {}\n".format(department[0], department[1], department[2], department[3]))
    
    # Display contents of employee Table
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    print("-- DISPLAYING Employee RECORDS --")
    for employee in employees:
        print("Employee ID: {}\nEmployee Name: {}\nDepartment ID: {}\nSalary : ${}\n".format(employee[0], employee[1], employee[2], employee[3]))

    # Display contents of Hours Worked Table
    cursor.execute("SELECT * FROM hours_worked")
    hoursWorked = cursor.fetchall()
    print("-- DISPLAYING Hours Worked RECORDS --")
    for weekHours in hoursWorked:
        print("Check Number: {}\nEmployee ID: {}\nWorked {} Hours, Week {}, Of Year {}\n".format(weekHours[0], weekHours[1], weekHours[4], weekHours[3], weekHours[2]))
    
    # Display contents of suppliers Table
    cursor.execute("SELECT * FROM suppliers")
    suppliers = cursor.fetchall()
    print("-- DISPLAYING Suppliers RECORDS --")
    for supplier in suppliers:
        print("Supplier ID: {}\nSupplier Name: {}\nPhone Number: {}\nAddress: {}\n".format(supplier[0], supplier[1], supplier[2], supplier[3]))

    # Display contents of supplies inventory Table
    cursor.execute("SELECT * FROM supplies_inventory")
    totalInventory = cursor.fetchall()
    print("-- DISPLAYING Inventory RECORDS --")
    for itemInventory in totalInventory:
        print("Item ID: {}\nItem Name: {}\nItem Quantity: {}\nLast Shipment: {}\nSupplier ID: {}]\n".format(itemInventory[0], itemInventory[1], itemInventory[2], itemInventory[3], itemInventory[4]))

    # Display contents of supplies orders Table
    cursor.execute("SELECT * FROM supplies_orders")
    orders = cursor.fetchall()
    print("-- DISPLAYING Supplies Orders RECORDS --")
    for order in orders:
        print("Order ID: {}\nItem ID: {}\nQuantity Bought: {}\nOrder Date: {}\nExpected Delivery Date: {}\nArrival Date: {}\n".format(order[0], order[1], order[2], order[3], order[4], order[5]))

    # Display contents of Distributors Table
    cursor.execute("SELECT * FROM distributors")
    distributors = cursor.fetchall()
    print("-- DISPLAYING distributors RECORDS --")
    for distributor in distributors:
        print("Distributor ID: {}\nDistributor Name: {}\nQuantity Ordered: {}\nQuantity Sold: {}\n".format(distributor[0], distributor[1], distributor[2], distributor[3]))

    # Display contents of Wines Table
    cursor.execute("SELECT * FROM wines")
    wines = cursor.fetchall()
    print("-- DISPLAYING wine RECORDS --")
    for wine in wines:
        print("Wine ID: {}\nWine Name: {}\nCurrent Quantity on Hand: {}\nDistributor ID: {}\n".format(wine[0], wine[1], wine[2], wine[3]))

    # Display contents of Wine Order Table
    cursor.execute("SELECT * FROM wine_orders")
    wineOrders = cursor.fetchall()
    print("-- DISPLAYING Wine Orders RECORDS --")
    for wineOrder in wineOrders:
        print("Order ID: {}\nWine ID: {}\nOrder Quantity: {}\nOrder Date: {}\n".format(wineOrder[0], wineOrder[1], wineOrder[2], wineOrder[3]))

try:
    cnx = mysql.connector.connect(**config)
    print("Connected to MySQL!")
    cursor = cnx.cursor()
    displayAllTableData()

    
except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")
    exit(1) 

cnx.close()