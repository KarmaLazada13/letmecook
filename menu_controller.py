# menu_controller.py
import os
from flask import request, redirect, url_for, current_app, render_template
from model.menu_model import MenuModel
from model.order_model import OrderModel


class MenuController:
    def __init__(self):
        self.model = MenuModel()

    def request_menu(self):
        menu_items = self.model.get_menu()
        return render_template("menu.html", items=menu_items)

    def create_menu(self):
        return render_template("menu_form.html")

    def store_menu(self):
        # Retrieve form data
        name = request.form.get("name")
        price = request.form.get("price")
        description = request.form.get("description")

        # Convert price to float
        if price:
            price = float(price)

        # Handle file upload
        image_file = request.files.get("image")
        image_filename = None

        if image_file and image_file.filename != "":
            # Optional: Validate file extension
            # e.g., only allow .jpg, .png, etc.
            allowed_extensions = {"jpg", "jpeg", "png", "gif"}
            ext = image_file.filename.rsplit(".", 1)[-1].lower()
            if ext in allowed_extensions:
                # Create a secure filename, store in static folder
                # Note: In production, consider using a unique name or timestamps
                image_filename = image_file.filename
                upload_path = os.path.join(
                    current_app.root_path, "static", "uploads", image_filename
                )
                image_file.save(upload_path)

        # Call model to store in DB
        self.model.store_menu(name, price, description, image_filename)

        # Redirect to the menu page
        return redirect(url_for("show_menu_list"))

    def list_menu(self):
        menu = self.model.get_menu()
        return render_template("list_menu.html", items=menu)

