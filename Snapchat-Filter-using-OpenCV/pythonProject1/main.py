from flask import *
from models.user import *

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/homeAction", methods=['POST'])
def homeAction():
    ulogin = request.form['ulogin']
    upassword = request.form['upassword']
    resultats = showUserByLogin(ulogin)
    if ulogin==resultats[1] and upassword==resultats[2]:
        return render_template("welcome.html", ulogin = ulogin, upassword = upassword)
    else:
        return "diso aii"
        #return render_template("wrong.html", ulogin=ulogin, upassword=upassword)


if __name__ == '__main__':
    #pour regarde l'erreur debug=true en mode production anaovana azy
    app.run(host="127.0.0.1", port="5000", debug=True)
    # app.run(debug=True)