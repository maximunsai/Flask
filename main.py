from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgre:pasword@localhost:5432/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db = SQLAlchemy(app)

class user(db.Model):
    id = db.column(db.Integer, primary_key =True)
    name = db.column(db.String(100), nullable = False)
    email =  db.column(db.String(150), unique = True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
    
@app.route('/')
def index():
    return 'Hello from Flask'


if __name__=='__main__':
    db.create_all()
    app.run(debug = True)






