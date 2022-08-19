from flask import *

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return render_template('home.html')

userDB=mysql.connector.connect(host="localhost", user="root", password="")

def homeAction():
    return "yeah"

@app.route("/welcome", methods=['POST'])
def welcome():
    result = request.form
    ulogin = result['Ulogin']
    upassword = result['Upassword']
    if ulogin=='nazirah' and upassword=='1234':
        return render_template("welcome.html", Ulogin=ulogin, Upassword=upassword)
    else:
        return "diso aii"


app.run(debug=True)
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

if __name__ == '__main__':
    #pour regarde l'erreur debug=true en mode production anaovana azy
    app.run(host="127.0.0.1", port=80, debug=True)
    # app.run(debug=True)
