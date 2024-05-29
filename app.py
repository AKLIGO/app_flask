from flask import Flask, render_template
from flask_cors import CORS
from extension import db
from models.user import User
from flask_migrate import Migrate

# Initialiser l'application Flask
app = Flask(__name__)
CORS(app)

#config DB port

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:akligo@localhost/projetflaskvue'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#initialisation de la BD
db.init_app(app)

migrate=Migrate(app,db)


# Définir une route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')


with app.app_context():
    db.create_all()

# Exécuter l'application
if __name__ == '__main__':
    app.run(debug=True)
