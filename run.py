import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #view
def index():
    return render_template("index.html")
    
@app.route('/about') #view
def about():
    return render_template("about.html")

@app.route('/contact') #view
def contact():
    return render_template("contact.html")
    
@app.route('/careers') #view
def careers():
    return render_template("careers.html")    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
            port=int(os.environ.get('PORT')), 
            debug=True) #need debug on to develop or changes wont show
            
