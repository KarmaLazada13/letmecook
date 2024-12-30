import sqlite3

def create_orders_table(db_path="database.db"):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Lệnh SQL để tạo bảng orders
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT NOT NULL,
            menu_id INTEGER NOT NULL,
            note TEXT,
            price REAL NOT NULL,  -- Sửa từ o.price thành price
            FOREIGN KEY (menu_id) REFERENCES menus (id)
        )
    """)
    
    connection.commit()
    connection.close()
    print("Created 'orders' table.")

if __name__ == "__main__":
    create_orders_table()
