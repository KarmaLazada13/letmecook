# order_controller.py
from flask import request, redirect, url_for, render_template
from model.order_model import OrderModel
from model.menu_model import MenuModel

class OrderController:
    def __init__(self):
        self.order_model = OrderModel()
        self.menu_model = MenuModel()

    def request_order_page(self):
        orders = self.order_model.get_orders()
        return render_template("order_list.html", orders=orders)

    def create_order_page(self):
        menu_items = self.menu_model.get_menu()
        return render_template("order_form.html", menu_items=menu_items)

    def store_order(self):
        customer = request.form.get("customer")
        menu_id = request.form.get("menu_id")
        note = request.form.get("note")
        price = request.form.get("price")

        self.order_model.create_order(customer, menu_id, note, price)
        return redirect(url_for("show_order_list"))



