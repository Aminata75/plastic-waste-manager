from flask import Flask, render_template, request, redirect
from PlasticWasteManager import PlasticWasteManager
from datetime import datetime
from utils import *
from UI_helper import PLASTIC_TYPES

app = Flask(__name__)

manager = PlasticWasteManager()

# 🏡 Home
@app.route("/")
def home():
    return render_template("home.html")


# ➕ ADD ITEM
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        plastic_type = request.form["plastic_type"]
        size = int(request.form["size"])
        sort_date = datetime.strptime(request.form["sort_date"], "%Y-%m-%d")

        manager.add_item(plastic_type, size, sort_date)

        return redirect("/inventory")
    
    return render_template("add.html", plastic_type=PLASTIC_TYPES)


# 📦 VIEW INVENTORY
@app.route("/inventory")
def inventory():
    manager.load_inventory()
    items = manager.inventory.values()
    return render_template("inventory.html", items=items)


# 🫴🏾 GET ITEM
@app.route("/item/<int:item_id>")
def view_item(item_id):
    manager.load_inventory()
    item = manager.get_item(item_id)

    return render_template("item.html", item=item)


# ❌ REMOVE ITEM
@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    manager.load_inventory()
    manager.remove_item(item_id)
    manager.save_inventory()

    return redirect("/inventory")


# ➕ UPDATE ITEM
@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    manager.load_inventory()
    item = manager.get_item(item_id)

    if not item:
        return "Item not found"

    if request.method == "POST":
        
        manager.update_item(
            item_id,
            plastic_type = request.form.get("plastic_type"),
            size = int(request.form.get("size")),
            sort_date = datetime.strptime(request.form.get("sort_date"), "%Y-%m-%d")
        )
        manager.save_inventory()

        return redirect("/inventory")
    
    return render_template("edit.html", item=item, plastic_type=PLASTIC_TYPES)


# 📈 STATS
@app.route("/stats")
def stats():
    manager.load_inventory()
    stats = manager.get_statistics()
    return render_template("stats.html", stats=stats)


if __name__ == "__main__":
    app.run(debug=True)

