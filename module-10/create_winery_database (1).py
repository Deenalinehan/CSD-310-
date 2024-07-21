import mysql.connector
import random as ran

# Database Configuration
config = {
    'user': 'root',
    'password': input("Provide your root password: "), 
    'host': '127.0.0.1',  
}

# this will generate CREATE TABLE statements
def createTables():
    tables = {
        'department': (
            "dept_id INT AUTO_INCREMENT PRIMARY KEY,"
            "dept_name VARCHAR(255) NOT NULL,"
            "dept_leader VARCHAR(255),"
            "employee_count INT"
        ),
        'employee': (
            "employee_id INT AUTO_INCREMENT PRIMARY KEY,"
            "employee_name VARCHAR(255) NOT NULL,"
            "dept_id INT,"  
            "salary DECIMAL(10,2),"      
            "FOREIGN KEY (dept_id) REFERENCES department(dept_id)"
        ),
        'hours_worked': ( 
            "check_number INT AUTO_INCREMENT PRIMARY KEY,"
            "employee_id INT,"
            "year INT,"
            "week INT,"
            "hours_worked DECIMAL(5,2),"
            "FOREIGN KEY (employee_id) REFERENCES employee(employee_id)"
        ),
        'suppliers': (
            "supplier_id INT AUTO_INCREMENT PRIMARY KEY,"
            "supplier_name VARCHAR(255),"
            "supplier_phone_number VARCHAR (20),"
            "supplier_address VARCHAR(255)"
        ),
        'supplies_inventory': (
            "item_id INT AUTO_INCREMENT PRIMARY KEY,"
            "item_name VARCHAR(255) NOT NULL,"
            "item_quantity INT,"
            "last_shipment DATE,"
            "supplier_id INT,"     
            "FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)"    
        ),
        'supplies_orders': (
            "order_id INT AUTO_INCREMENT PRIMARY KEY,"
            "item_id INT,"
            "quantity_bought INT,"
            "order_date DATE,"
            "expected_delivery_date DATE,"
            "arrival DATE,"
            "FOREIGN KEY (item_id) REFERENCES supplies_inventory(item_id)"
        ),
        'distributors': (
            "dist_id INT AUTO_INCREMENT PRIMARY KEY,"
            "dist_name VARCHAR(255) NOT NULL,"
            "quantity_ordered INT,"
            "quantity_sold INT"
        ),
        'wines': (
            "wine_id INT AUTO_INCREMENT PRIMARY KEY,"
            "wine_name VARCHAR(255) NOT NULL,"
            "current_quantity INT,"
            "dist_id INT,"
            "FOREIGN KEY (dist_id) REFERENCES distributors(dist_id)"
        ),
        'wine_orders': (
            "order_id INT AUTO_INCREMENT PRIMARY KEY,"
            "wine_id INT,"
            "order_quantity INT,"
            "order_date DATE,"
            "FOREIGN KEY (wine_id) REFERENCES wines(wine_id)"
        )
    }

    for table_name, fields in tables.items():
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        print(f"\n--- SQL for {table_name.upper()} ---")
        print(f"CREATE TABLE {table_name} ({fields})")
        cursor.execute(create_table_query)

# These functions each add the data to there corresponding table
def addDepartmentInfo():
    sql = "INSERT INTO department (dept_name, dept_leader, employee_count) VALUES (%s, %s, %s)"
    val = [
        ('Finance', 'Janet collins', 1 ),
        ('Marketing', 'Roz Murphy', 2 ),
        ('Distribution', 'Henry Doyle', 1 ),
        ('Production', 'Maria Costanza', 21 ),
    ]
    cursor.executemany(sql, val)

def addEmployeeInfo():
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary) 
        VALUES ('Janet collins', (SELECT dept_id FROM department WHERE dept_name = "Finance"), 67232.22)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Roz Murphy', (SELECT dept_id FROM department WHERE dept_name = "Marketing"), 54067.22)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Henry Doyle', (SELECT dept_id FROM department WHERE dept_name = "Distribution"), 82432.22)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Maria Costanza', (SELECT dept_id FROM department WHERE dept_name = "production"), 152232.22)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Bob Ulrich', (SELECT dept_id FROM department WHERE dept_name = "Marketing"), 42232.22)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Spencer Stark', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('George Stavos', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Mariah Perry', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Loui Rancher', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Hulk Honan', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Joffery Lanister', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Tony Tiger', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Robert Diniro', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Alex Harper', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Robert Lopez', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Winston Churchill', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Alex Garcia', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Ralphy R-Rey', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Dominic Cruise', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Christion Ronaldo', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Ludwig Aghren', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Linus Sebastion', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Luke Dreamer', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Gandolf White', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)
    cursor.execute("""
        INSERT INTO employee (employee_name, dept_id, salary)
        VALUES ('Pippen Took', (SELECT dept_id FROM department WHERE dept_name = "production"), 40241.40)
    """)

def addHoursWorked():
    for week in range(12):
        hoursWorked = ran.uniform(30, 60)
        cursor.execute("""
        INSERT INTO hours_worked (employee_id, year, week, hours_worked) 
        VALUES ((SELECT employee_id FROM employee WHERE employee_name = "Henry Doyle"), 2024, {}, {})
""".format(week+1, hoursWorked))
    for week in range(12):
        hoursWorked = ran.uniform(40, 70)
        cursor.execute("""
        INSERT INTO hours_worked (employee_id, year, week, hours_worked) 
        VALUES ((SELECT employee_id FROM employee WHERE employee_name = "Janet collins"), 2024, {}, {})
""".format(week+1, hoursWorked))
    for week in range(12):
        hoursWorked = ran.uniform(30, 60)
        cursor.execute("""
        INSERT INTO hours_worked (employee_id, year, week, hours_worked) 
        VALUES ((SELECT employee_id FROM employee WHERE employee_name = "Roz Murphy"), 2024, {}, {})
""".format(week+1, hoursWorked))
    for week in range(12):
        hoursWorked = ran.uniform(30, 60)
        cursor.execute("""
        INSERT INTO hours_worked (employee_id, year, week, hours_worked) 
        VALUES ((SELECT employee_id FROM employee WHERE employee_name = "Maria Costanza"), 2024, {}, {})
""".format(week+1, hoursWorked))
    for week in range(12):
        hoursWorked = ran.uniform(30, 60)
        cursor.execute("""
        INSERT INTO hours_worked (employee_id, year, week, hours_worked) 
        VALUES ((SELECT employee_id FROM employee WHERE employee_name = "Bob Ulrich"), 2024, {}, {})
""".format(week+1, hoursWorked))

def addSuppliers():
    sql = "INSERT INTO suppliers (supplier_name, supplier_phone_number, supplier_address) VALUES (%s, %s, %s)"
    val = [
    ('Cork Supply', '1-423-543-7342', '123 Momba Ave, Santa Cruis, California, 55435' ),
    ('Label Supply', '1-777-444-7777', '442 Curtis Street, Albany, Oregon, 25234' ),
    ('Tubs', '1-343-5253-2344', '5277 Meta Parkway, New Mexico, 63245' )
    ]

    cursor.executemany(sql, val)

def addSupplies():
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('500ML Wine Bottles', 152, '2024-6-14', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Cork Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('750ML Wine Bottles', 102, '2024-6-14', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Cork Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('1.5L Wine Bottles', 63, '2024-6-14', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Cork Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('Bottle Corks', 256, '2024-6-14', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Cork Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('500ML Wine Labels', 553, '2024-5-25', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Label Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('750ML Wine Labels', 1202, '2024-5-25', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Label Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('1.5L Wine Labels', 743, '2024-5-25', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Label Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('500ML 6Ct Box', 22, '2024-5-25', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Label Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('750ML 6Ct Box', 73, '2024-5-25', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Label Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('1.5L 6Ct Box', 43, '2024-5-25', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Label Supply"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('Wine Vats', 4, '2024-4-2', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Tubs"))
    """)
    cursor.execute("""
        INSERT INTO supplies_inventory (item_name, item_quantity, last_shipment, supplier_id) 
        VALUES ('100 Ft Plastic Tubing Roll', 1, '2024-4-2', (SELECT supplier_id FROM suppliers WHERE supplier_name = "Tubs"))
    """)

def addSuppliesOrders():
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = '750ML Wine Bottles'), 300, '2024-5-1', '2024-6-2', '2024-6-14')
    """)
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = '1.5L Wine Bottles'), 100, '2024-5-1', '2024-6-2' ,'2024-6-14')
    """)
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = '500ML Wine Bottles'), 300, '2024-5-1', '2024-6-2' ,'2024-6-14')
    """)
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = 'Bottle Corks'), 1000, '2024-5-1', '2024-6-2' ,'2024-6-14')
    """)
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = '500ML Wine Labels'), 1000, '2024-4-16', '2024-5-27', '2024-5-25')
    """)
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = '750ML Wine Labels'), 1500, '2024-4-16', '2024-5-27' ,'2024-5-25')
    """)
    cursor.execute("""
        INSERT INTO supplies_orders (item_id, quantity_bought, order_date, expected_delivery_date, arrival) 
        VALUES ((SELECT item_id FROM supplies_inventory WHERE item_name = '1.5L Wine Labels'), 900, '2024-4-16', '2024-5-27' ,'2024-5-25')
    """)

def addDistributors():

    sql = "INSERT INTO distributors (dist_name, quantity_ordered, quantity_sold) VALUES (%s, %s, %s)"
    val = [
    ('Hyvee', 2323, 212),
    ('Wine Online', 6243, 5323),
    ('Wine Is Us', 421, 413),
    ('Wine About It', 5243, 4432)
    ]

    cursor.executemany(sql, val)

def addWines():

    cursor.execute("""
        INSERT INTO wines (wine_name, current_quantity, dist_id) 
        VALUES ('Bacchus Merlot', 200 , (SELECT dist_id FROM distributors WHERE dist_name = 'Hyvee'))
    """)
    cursor.execute("""
        INSERT INTO wines (wine_name, current_quantity, dist_id) 
        VALUES ('Bacchus Cabernet', 341 , (SELECT dist_id FROM distributors WHERE dist_name = 'Wine Online'))
    """)
    cursor.execute("""
        INSERT INTO wines (wine_name, current_quantity, dist_id) 
        VALUES ('Bacchus Chablis', 122 , (SELECT dist_id FROM distributors WHERE dist_name = 'Wine Is Us'))
    """)
    cursor.execute("""
        INSERT INTO wines (wine_name, current_quantity, dist_id) 
        VALUES ('Bacchus Chardonnay', 54 , (SELECT dist_id FROM distributors WHERE dist_name = 'Wine About It'))
    """)

def addWineOrders():
    cursor.execute("""
        INSERT INTO wine_orders (wine_id, order_quantity, order_date) 
        VALUES ((SELECT wine_id FROM wines WHERE wine_name = 'Bacchus Merlot'), 60, '2024-6-29')
    """)
    cursor.execute("""
        INSERT INTO wine_orders (wine_id, order_quantity, order_date) 
        VALUES ((SELECT wine_id FROM wines WHERE wine_name = 'Bacchus Merlot'), 60, '2024-5-29')
    """)
    cursor.execute("""
        INSERT INTO wine_orders (wine_id, order_quantity, order_date) 
        VALUES ((SELECT wine_id FROM wines WHERE wine_name = 'Bacchus Merlot'), 60, '2024-4-29')
    """)
    cursor.execute("""
        INSERT INTO wine_orders (wine_id, order_quantity, order_date) 
        VALUES ((SELECT wine_id FROM wines WHERE wine_name = 'Bacchus Cabernet'), 180, '2024-5-15')
    """)
    cursor.execute("""
        INSERT INTO wine_orders (wine_id, order_quantity, order_date) 
        VALUES ((SELECT wine_id FROM wines WHERE wine_name = 'Bacchus Chardonnay'), 240, '2024-4-10')
    """)
    cursor.execute("""
        INSERT INTO wine_orders (wine_id, order_quantity, order_date) 
        VALUES ((SELECT wine_id FROM wines WHERE wine_name = 'Bacchus Chablis'), 480, '2024-3-20')
    """)


# Connection
try:
    cnx = mysql.connector.connect(**config)
    print("Connected to MySQL!")
    cursor = cnx.cursor()
    # This deletes any database of the same name created prior to running script.
    cursor.execute("DROP DATABASE IF EXISTS bacchus_winery")
    # this creates the database (if it doesn't exist)
    cursor.execute("CREATE DATABASE bacchus_winery")
    cnx.database = 'bacchus_winery'# this switches to the newly created database

    # Each of these run there coresponding 
    createTables()
    addDepartmentInfo()
    addEmployeeInfo()
    addHoursWorked()
    addSuppliers()
    addSupplies()
    addSuppliesOrders()
    addDistributors()
    addWines()
    addWineOrders()
    cnx.commit()
    
except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")
    exit(1) 

# commit the changes
# cnx.commit()
# Close the connection
cnx.close()
