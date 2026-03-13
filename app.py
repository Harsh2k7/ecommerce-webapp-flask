from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# -------- DATABASE CONNECTION --------

db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="ecommerce"
)

cursor = db.cursor()


# -------- REGISTER USER --------

@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["password"]

    sql = "INSERT INTO users(username,password) VALUES(%s,%s)"

    cursor.execute(sql,(username,password))

    db.commit()

    return jsonify({"message":"User Registered Successfully"})


# -------- LOGIN USER --------

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"

    cursor.execute(sql,(username,password))

    user = cursor.fetchone()

    if user:
        return jsonify({"message":"Login Successful"})
    else:
        return jsonify({"message":"Invalid Username or Password"})


# -------- GET PRODUCTS --------

@app.route("/products", methods=["GET"])
def get_products():

    cursor.execute("SELECT * FROM products")

    rows = cursor.fetchall()

    product_list = []

    for r in rows:

        product_list.append({
            "id": r[0],
            "name": r[1],
            "price": r[2],
            "image": r[3]
        })

    return jsonify(product_list)


# -------- SAVE ORDER --------

@app.route("/order", methods=["POST"])
def save_order():

    username = request.form["username"]
    product = request.form["product"]
    price = request.form["price"]

    sql = "INSERT INTO orders(username,product,price) VALUES(%s,%s,%s)"

    cursor.execute(sql,(username,product,price))

    db.commit()

    return jsonify({"message":"Order Saved Successfully"})


# -------- USER ORDER HISTORY --------

@app.route("/orders/<username>", methods=["GET"])
def order_history(username):

    sql = "SELECT product,price FROM orders WHERE username=%s"

    cursor.execute(sql,(username,))

    rows = cursor.fetchall()

    orders = []

    for r in rows:

        orders.append({
            "product": r[0],
            "price": r[1]
        })

    return jsonify(orders)


# -------- RUN SERVER --------

if __name__ == "__main__":
    app.run(debug=True)