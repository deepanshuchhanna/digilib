from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():

    return render_template('login.html')

@app.route('/register')
def about():
    return "About page"

if __name__=="__main__":

    app.run(debug=True)             #used not to run every time we just have to refresh only