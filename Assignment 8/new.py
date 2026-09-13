#Import
from flask import Flask, render_template, request

#Interact
web = Flask(__name__)

#Map
@web.route('/')
@web.route('/register')
#Input
def homepage():
    return render_template('register.html')

#Map
@web.route("/confirmation", methods = ['POST', 'GET'])

#Input
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phonenumber')
        return render_template('confirm.html', name = n, city = c, phonenumber = p)



#Main
if __name__ == "__main__":
    web.run(debug=True)

