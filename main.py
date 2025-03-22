from flask import Flask, render_template, request, redirect
from mydb import session, User
from datetime import datetime
app = Flask(__name__)



@app.route("/", methods=['GET'])
def home():
    users = session.query(User).all()
    return render_template('index.html',users = users)

@app.route("/register", methods=['POST'])
def signup():
    if request.method == "POST":
        user = User(name=request.form['name'], email=request.form['email'], phone=request.form['phone'])
        session.add(user)
        session.commit()
        return redirect("/")
@app.route("/edit/<int:id>", methods=['GET'])
def edit(id):
    users = session.query(User).all()
    return render_template('index.html', edit_id = id, users = users)

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    session.query(User).filter_by(id=id).delete()
    session.commit()
    users = session.query(User).all()
    return render_template('index.html', users = users)

@app.route("/addnew", methods=['GET'])
def addnew():
    users = session.query(User).all()
    return render_template('index.html', addNewuser = True, users = users)

@app.route("/update/<int:id>", methods=['POST'])
def update(id):
    user = session.query(User).filter_by(id=id).first()
    user.name = request.form['name']
    user.email = request.form['email']
    user.phone = request.form['phone']
    session.commit()
    return redirect("/")

@app.route("/search", methods=['POST'])
def search():
    search = request.form['search']
    users = session.query(User).filter(User.name.like(f'%{search}%')).all()
    return render_template('index.html', users = users)

if __name__ == "__main__":
    app.run(debug=True, port=8000)