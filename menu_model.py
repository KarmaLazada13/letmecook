# menu_model.py
import sqlite3

class MenuModel:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path

    def store_menu(self, name, price, description, image_filename=None):
        """
        Insert a new menu item into the 'menus' table.
        `image_filename` is the name of the uploaded file (or None if not provided).
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO menus (name, price, description, image)
            VALUES (?, ?, ?, ?)
        """, (name, price, description, image_filename))

        connection.commit()
        connection.close()

    def get_menu(self):
        """
        Fetch all menu items.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT id, name, price, description, image FROM menus")
        results = cursor.fetchall()

        connection.close()

        menu_items = []
        for row in results:
            item_id, name, price, description, image = row
            menu_items.append({
                "id": item_id,
                "name": name,
                "price": price,
                "description": description,
                "image": image
            })
        return menu_items
