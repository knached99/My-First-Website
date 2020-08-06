from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ =="__main__":
    #If any bugs are found, they'll popup in the webpage
    app.run(debug=True)