from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Welcome to the Home Page!'

# @app.route('/about')
# def about():
#     return 'This is the About Page.'

# ##http://127.0.0.1:5000/about

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import request

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)