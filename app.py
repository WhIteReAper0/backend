from flask import Flask
from todo.routes import task_bp
app = Flask(__name__)

app.register_blueprint(task_bp)


@app.route('/')
def main():
    return '<h1>Homepage<h1>'


if __name__ == '__main__':
    app.run(debug=True)
