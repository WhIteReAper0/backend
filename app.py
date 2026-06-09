from flask import Flask, jsonify 

from todo.routes import task_bp
from auth.templates.routes import auth_bp

from flask_login import LoginManager

from database.engine import db   
from database.models.todo import Task
from database.models.auth import User 

app = Flask(__name__)
login_manager = LoginManager()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fgsfds'


db.init_app(app)
login_manager.init_app(app)


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(id=int(user_id)).first()



app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')



if __name__ == '__main__':
    app.run(debug=True)

