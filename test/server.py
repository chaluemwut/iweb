from flask import Flask
from flask.templating import render_template
from test.simple_controller import simple

app = Flask(__name__)
app.register_blueprint(simple)

@app.route("/", methods=['POST', 'GET'])
def index():
    return 'Hello simple'

if __name__ == "__main__":
    app.run()