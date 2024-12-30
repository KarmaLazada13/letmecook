# order_model.py
import sqlite3

class OrderModel:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def create_order(self, customer, menu_id, note, price):
        """
        Insert a new order into the 'orders' table.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO orders (customer, menu_id, note, price)
                VALUES (?, ?, ?, ?)
            """, (customer, menu_id, note, price))

            connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating order: {e}")
        finally:
            connection.close()

    def get_orders(self):
        """
        Fetch all orders with their corresponding menu names.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            cursor.execute("""
                SELECT 
                    o.id AS order_id,
                    o.customer,
                    o.menu_id,
                    o.note,
                    o.price,
                    m.name AS menu_name
                FROM orders o
                LEFT JOIN menus m ON o.menu_id = m.id
            """)
            results = cursor.fetchall()

            orders = [
                {
                    "id": row[0],
                    "customer": row[1],
                    "menu_id": row[2],
                    "note": row[3],
                    "price": row[4],
                    "menu_name": row[5] if row[5] else "Unknown"
                }
                for row in results
            ]
            return orders
        except sqlite3.Error as e:
            print(f"Error fetching orders: {e}")
            return []
        finally:
            connection.close()