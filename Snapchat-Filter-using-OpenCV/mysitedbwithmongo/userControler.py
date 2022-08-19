from flask import *
from models.user import userDb


app = Flask(__name__)


@app.route("/")
def home():
    user = userDb()
    utilisateur = user.find_one({'nom':'Nazirah'})
    print(utilisateur)
    return render_template('home.html', user=utilisateur)


if __name__=="__main__":
    app.run(host="localhost", port=5000, debug=True)