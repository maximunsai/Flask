from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:pasword@localhost:5432/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db = SQLAlchemy(app)

class User(db.Model):
    Id = db.column(db.Integer, primary_key =True)
    username = db.column(db.String(100), nullable = False)
    email =  db.column(db.String(150), unique = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("list.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("create.html")

@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("detail.html", user=user)

@app.route("/user/delete/<int:id>", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("delete.html", user=user)
   


if __name__=='__main__':
    db.create_all()
    app.run(debug = True)






