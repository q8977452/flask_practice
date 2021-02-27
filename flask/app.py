from flask import Flask
import auth

app = Flask(__name__)
auth.init_app(app)


@app.route('/')
def index():
    return 'foo'


if __name__ == "__main__":
    app.run(debug=True)