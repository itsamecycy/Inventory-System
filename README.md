# Python Inventory Management System

A simple inventory management system built with **Python** and **MySQL**. This project allows users to manage products, track stock quantities, update product information, and calculate the total value of their inventory through a terminal-based menu.

## Features

- **Add Products** — Add new products with an ID, name, price, and quantity.
- **Remove Products** — Remove products from the inventory using their product ID.
- **Search Products** — Find a product by its ID.
- **Display Inventory** — View the products stored in the database.
- **Update Products** — Update product names, prices, and stock quantities.
- **Calculate Inventory Value** — Calculate the combined value of all products in stock.
- **Low Stock Report** — Identify products with quantities at or below the configured threshold.
- **MySQL Integration** — Store product information in a MySQL database so records persist after the program closes.

## Technologies Used

- Python
- MySQL
- MySQL Connector/Python
- `python-dotenv`
- Git and GitHub

## Project Structure

```text
Inventory_system/
├── .venv/              # Python virtual environment (not committed)
├── .env                # Database credentials (not committed)
├── .gitignore          # Files excluded from Git
├── inventory.py        # Inventory and database operations
├── main.py             # Main menu and program entry point
├── product.py          # Product class
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Requirements

Before running the project, install:

- Python 3.14 or another compatible Python version
- MySQL Server
- MySQL Workbench (optional, for managing and viewing the database)
- Git (optional, for cloning the repository)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/itsamecycy/Inventory-System.git
cd Inventory-System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create the MySQL database

Make sure your MySQL Server is running. Open MySQL Workbench or another MySQL client and execute the SQL script in `schema.sql`.

Alternatively, run the following command from your project directory in a terminal:

```bash
mysql -u your_mysql_username -p < schema.sql
```

Replace `your_mysql_username` with your MySQL username. Enter your password when prompted.

This creates the `inventory_system` database and the `products` table if they do not already exist.

### 5. Configure the environment variables

Create a `.env` file in the project root. Add your own MySQL credentials:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=inventory_system
```

Replace the example username and password with your actual MySQL credentials. Make sure the variable names match those used in `inventory.py`.

**Security:** Never commit your `.env` file or publish your database password to GitHub.

### 6. Run the application

With the virtual environment activated, run:

```bash
python main.py
```

## Menu Options

When the application starts, you can select from these options:

| Option | Function |
|---|---|
| 1 | Add Product |
| 2 | Remove Product |
| 3 | Search Product |
| 4 | Display Inventory |
| 5 | Update Product |
| 6 | Calculate Total Inventory Value |
| 7 | Stock Report |
| 8 | Exit |

## Database

The application uses a MySQL database named `inventory_system` and a table named `products`.

| Column | Type | Description |
|---|---|---|
| `id` | INT | Unique product identifier and primary key |
| `name` | VARCHAR(100) | Product name |
| `price` | DECIMAL(10,2) | Product price |
| `quantity` | INT | Available stock quantity |

Product records are stored in MySQL rather than only in memory, allowing the data to remain available between application runs.

## Future Improvements

- Add input validation and more detailed error handling.
- Implement product categories and supplier information.
- Add inventory transaction history.
- Introduce user authentication and role-based access.
- Develop a graphical user interface or web interface.
- Add automated tests for inventory and database operations.

## Author

Developed as a Python programming project to practice object-oriented programming, database integration, SQL, and version control.
