# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return "HEllo."

from flaskr import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8089)