# app.py

from flask import Flask, render_template, request
from controller.menu_controller import MenuController
from controller.order_controller import OrderController

app = Flask(__name__)

@app.route("/")
def show_menu():
    controller = MenuController()
    return controller.request_menu()


# as BACK SYSTEM
@app.route("/admin/menu/list")
def show_menu_list():
    controller = MenuController()
    return controller.list_menu()

@app.route("/admin/menu/create")
def create_menu():
    controller = MenuController()
    return controller.create_menu()

@app.route("/admin/menu/store", methods=['POST'])
def store_menu():
    controller = MenuController()
    return controller.store_menu()

@app.route("/admin/order")
def show_order_list():
    controller = OrderController()
    return controller.request_order_page()

@app.route("/admin/order/create")
def create_order():
    controller = OrderController()
    return controller.create_order_page()

@app.route("/admin/order/store", methods=['POST'])
def store_order():
    controller = OrderController()
    return controller.store_order()

if __name__ == "__main__":
    app.run(debug=True)