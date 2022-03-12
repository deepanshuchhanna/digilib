import os
import requests

from flask import Flask,render_template,session,request,redirect,url_for,jsonify,abort,Response
# from cs50 import sql
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps
# from flask import g


app = Flask(__name__)
app.debug = True
app.secret_key = 'LIBRARY_MANAGEMENT'

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def login_required(f):
	@wraps(f)
	def decorated_function(*args,**kwrags):
		if "user" not in session:
			return redirect(url_for('login',next=request.url))
		return f(*args,**kwrags)
	return decorated_function

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user")
def user():
	if "user" in session:
		user=session["user"]
		name=str(user)
		name=name[2:-3]
		return render_template("logout.html")
	else:
		return redirect('/login')

@app.route("/logout")
def logout():
	session.pop('user',None)
	return redirect(url_for('login'))

@app.route("/login")
def login():
	if "user" in session:
		return redirect('/user')
	else:
		return render_template('login.html')

@app.route("/logging",methods=["POST"])
def logging():
	u_id=request.form.get("id")
	pword=request.form.get("password")
	user=db.execute("SELECT userid FROM all_user WHERE userid=:userid AND password=:password",{"userid":u_id,"password":pword}).fetchone()
	if user is None:
		return Response("ERROR!...No such user found")
	session["user"]=user
	return redirect(url_for("user"))

@app.route("/register")
def register():
	return render_template('register.html')

@app.route("/registering",methods=["POST"])
def registering():
	user_id=request.form.get("id")
	password=request.form.get("password")
	users=db.execute("SELECT * FROM all_user WHERE userid=:userid",{"userid":user_id}).fetchall()
	if len(users) >0:
		return Response("Username Already Taken...")
	db.execute("INSERT INTO all_user(userid,password) VALUES (:userid,:password)",{"userid":user_id,"password":password})
	db.commit()
	return redirect("/user")

@app.route("/newspaper")
@login_required
def newspaper():
	return render_template('newspaper.html')

@app.route("/ebooks")
@login_required
def ebooks():
	return render_template('ebooks.html')


@app.route("/feedback")
@login_required
def feedback():
	return render_template('feedback.html')


@app.route("/about")
@login_required
def about():
	return render_template('about.html')

@app.route("/physics")
@login_required
def physics():
	return render_template('books/physics.html')

@app.route("/chemistry")
@login_required
def chemistry():
	return render_template('books/chemistry.html')

@app.route("/bee")
@login_required
def bee():
	return render_template('books/bee.html')

@app.route("/atlas")
@login_required
def atlas():
	return render_template('books/atlas.html')

@app.route("/env")
@login_required
def env():
	return render_template('books/env.html')

@app.route("/geoindia")
@login_required
def geoindia():
	return render_template('books/geoindia.html')

@app.route("/india")
@login_required
def india():
	return render_template('books/india.html')

@app.route("/math")
@login_required
def math():
	return render_template('books/math.html')

@app.route("/modern")
@login_required
def modern():
	return render_template('books/modern.html')

@app.route("/pps")
@login_required
def pps():
	return render_template('books/pps.html')



@app.route("/feedback1",methods=["POST"])       #feedback data base     and @app.route is a URL
def feedback1():
	fname=request.form.get("fname")
	lname=request.form.get("lname")
	country=request.form.get("country")
	email=request.form.get("email")
	fback=request.form.get("fback")
	
	db.execute("INSERT INTO feedbacks(fname,lname,country,email,fback) VALUES (:fname,:lname,:country,:email,:fback)",{"fname":fname,"lname":lname,"country":country,"email":email,"fback":fback})
	db.commit()
	return Response("feedback submitted...")



if __name__=="__main__":
	app.run()