from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import datetime
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'inventory'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/location")
def location():
    return render_template("location.html")


@app.route("/product")
def product_location():
    con = mysql.connect()
    cursor = con.cursor()
    local = "SELECT * FROM location"
    cursor.execute(local)
    locations = cursor.fetchall()
    return render_template("products.html", title='Location', locations=locations)


@app.route("/movement")
def product_movement():
    con = mysql.connect()
    cursor = con.cursor()
    local = "SELECT * FROM location"
    cursor.execute(local)
    locations = cursor.fetchall()
    return render_template("product_movement.html", title='Location', locations=locations)


@app.route("/", methods=['POST'])
def register_db():
    con = mysql.connect()
    cursor = con.cursor()
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    if email == "" or password == "" or username == "":
        return "<script>window.alert('Check All fields');window.location='/';</script>"
    else:

        values = "INSERT INTO `login`(`username`,`email`, `password`) VALUES('" + username + "','" + email + "','" + password + "')"
        print(values)
        cursor.execute(values)
        con.commit()
        con.close()
        return "<script>window.alert('Registration Successfully');window.location='/login';</script>"


@app.route("/login", methods=['POST'])
def login_db():
    email = request.form['email']
    password = request.form['password']
    if email == "" or password == "":
        return "<script>window.alert('Check All fields');window.location='/loc';</script>"
    else:

        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * FROM login WHERE email='" + email + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            return "<script>window.alert('Invalid username and password');window.location='/';</script>"
        else:
            return "<script>window.alert('Login Successfully');window.location='/home';</script>"


@app.route("/location", methods=['GET', 'POST'])
def location_manages():
    if request.form['button'] == "Add":
        con = mysql.connect()
        cursor = con.cursor()
        location_id = request.form['id']
        location_name = request.form['name']
        if location_id == "" or location_name == "":
            return "<script>window.alert('Check All fields');window.location='/location';</script>"
        else:
            values = "INSERT INTO `location`(`loc_id`, `loc_name`) VALUES('" + location_id + "','" + location_name + "')"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Location Added Successfully');window.location='/location';</script>"
    if request.form['button'] == "Delete":
        location_id = request.form['id']
        if location_id == "":
            return "<script>window.alert('Check All fields');window.location='/location';</script>"
        else:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * FROM location WHERE loc_id='" + location_id + "'")
            data = cursor.fetchone()
            values = "DELETE FROM `location` WHERE loc_id='" + location_id + "'"
            if data is None:
                return "<script>window.alert('Invalid Location ID');window.location='/location';</script>"
            else:
                con = mysql.connect()
                cursor = con.cursor()
                values = "DELETE FROM `location` WHERE loc_id='" + location_id + "'"
                cursor.execute(values)
                con.commit()
                con.close()
                return "<script>window.alert('Location Deleted Successfully');window.location='/location';</script>"
    if request.form['button'] == "Update":
        location_id = request.form['id']
        location_name = request.form['name']
        if location_id == "" or location_name == "":
            return "<script>window.alert('Check All fields');window.location='/location';</script>"
        else:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * FROM location WHERE loc_id='" + location_id + "'")
            data = cursor.fetchone()
            values = "UPDATE `location` SET `loc_name`='" + location_name + "' WHERE loc_id='" + location_id + "'"
            if data is None:
                return "<script>window.alert('Invalid Location ID');window.location='/location';</script>"
            else:
                con = mysql.connect()
                cursor = con.cursor()
                values = "UPDATE `location` SET `loc_name`='" + location_name + "' WHERE loc_id='" + location_id + "'"
                cursor.execute(values)
                con.commit()
                con.close()
                return "<script>window.alert('Location Updated Successfully');window.location='/location';</script>"
    if request.form['button'] == "View_All":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM location")
        locations = cursor.fetchall()
        return render_template("view_all_location.html", locations=locations)


@app.route("/product", methods=['GET', 'POST'])
def product_manages():
    if request.form['button'] == "Add":
        con = mysql.connect()
        cursor = con.cursor()
        product_id = request.form['id']
        name = request.form['name']
        prod_location = request.form['location']
        quantity = request.form['qty']
        if product_id == "" or name == "" or prod_location == "--select--" or quantity == "":
            return "<script>window.alert('Check All fields');window.location='/product';</script>"
        else:
            print(product_id + " " + name + " " + prod_location + " " + quantity)
            values = "INSERT INTO `product`(`prod_id`, `prod_name`,`place`,`qty`) VALUES('" + product_id + "','" + name + "','" + prod_location + "','" + quantity + "')"
            cursor.execute(values)
            con.commit()
            con.close()
            return "<script>window.alert('Location Added Successfully');window.location='/product';</script>"
    if request.form['button'] == "Delete":
        product_id = request.form['id']
        if product_id == "":
            return "<script>window.alert('Check Product Id Detail');window.location='/product';</script>"
        else:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * FROM product WHERE prod_id='" + product_id + "'")
            data = cursor.fetchone()
            values = "DELETE FROM `product` WHERE prod_id='" + product_id + "'"
            if data is None:
                return "<script>window.alert('Invalid Product ID');window.location='/product';</script>"
            else:
                con = mysql.connect()
                cursor = con.cursor()
                values = "DELETE FROM `product` WHERE prod_id='" + product_id + "'"
                cursor.execute(values)
                con.commit()
                con.close()
                return "<script>window.alert('Product Deleted " \
                       "Successfully');window.location='/product';</script> "
    if request.form['button'] == "Update":
        product_id = request.form['id']
        product_name = request.form['name']
        prod_location = request.form['location']
        quantity = request.form['qty']
        if product_id == "" or product_name == "" or prod_location == "--select--" or quantity == "":
            return "<script>window.alert('Check All fields');window.location='/product';</script>"
        else:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * FROM product WHERE prod_id='" + product_id + "'")
            data = cursor.fetchone()
            values = "UPDATE `product` SET `prod_name`='" + product_name + "' WHERE prod_id='" + product_id + "' AND place='"+prod_location+"'"
            print(values)
            if data is None:
                return "<script>window.alert('Invalid Product ID');window.location='/product';</script>"
            else:
                con = mysql.connect()
                cursor = con.cursor()
                values = "UPDATE `product` SET `prod_id`='" + product_id + "',`prod_name`='" + product_name + "',`place`='" + prod_location + "',`qty`='" + quantity + "' WHERE prod_id='" + product_id + "'"
                cursor.execute(values)
                con.commit()
                con.close()
                return "<script>window.alert('Product Updated " \
                       "Successfully');window.location='/product';</script> "
    if request.form['button'] == "View_All":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        return render_template("view_all_product.html", products=products)


@app.route("/movement", methods=['GET', 'POST'])
def product_movements():
    if request.form['button'] == "Move":
        con = mysql.connect()
        cursor = con.cursor()
        product_id=request.form['id'];
        from_location=request.form['from'];
        to_location=request.form['to'];
        qty=request.form['qty'];

        select = "SELECT * FROM product WHERE prod_id='" + product_id+ "' AND place='" + from_location + "'"
        cursor.execute(select)

        product = cursor.fetchone()
        name=str(product[1])
        print(product[3]-int(qty))
        if product[3] == 0 or product[3]<int(qty):
            return "<script>window.alert('No quantity available');window.location='/movement';</script>"
        else:
            diff = product[3] - int(qty)
            if diff < 0:
                return "<script>window.alert('No quantity available');window.location='/movement';</script>"
            else:
                val2="UPDATE `product` SET `qty`='"+str(diff)+"' WHERE `prod_id`='"+product_id+"'AND `place`='"+from_location+"'"
                cursor.execute(val2)

                date = str(datetime.datetime.now())[:10]

                query = "INSERT INTO `product_movement`(`movementid`,`timestamp`, `from_location`, `to_location`, `product_id`, `qty`) VALUES (NULL,'"+date+"','"+from_location+"','"+to_location+"','"+request.form['id']+"','"+request.form['qty']+"')"

                cursor.execute(query)

                query1 = "SELECT * FROM product WHERE prod_id='" + product_id + "' AND place='" + to_location + "'"
                cursor.execute(query1)
                record1 = cursor.fetchone()
                print(record1)
                if record1 is None:
                    print(product_id+" "+name+" "+to_location+" "+qty)
                    values = "INSERT INTO `product`(`prod_id`, `prod_name`,`place`,`qty`) VALUES('" + product_id + "','" + name + "','" + to_location + "','" + qty + "')"
                    cursor.execute(values)
                    con.commit()
                    con.close()
                else:
                    add = record1[3] + int(qty)
                    val4 = "UPDATE `product` SET `qty`='" + str(add) + "' WHERE prod_id='" + product_id + "' and place='" + request.form['to'] + "'"
                    cursor.execute(val4)
                    con.commit()
                    con.close()
                return "<script>window.alert('Product moved successfully');window.location='/movement';</script>"

    if request.form['button'] == "View_All":
        con = mysql.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM product_movement")
        products = cursor.fetchall()
        return render_template("view_all_movements.html", products=products)


if __name__ == "__main__":
    app.run()
