from iweb.controller import APIController
from flask import Blueprint, Flask
from iweb import iWeb

app_name = '/simple'
simple = Blueprint('simple', __name__)

app = Flask(__name__)
app.register_blueprint(simple)

app.config['db.host'] = 'localhost'
app.config['db.name'] = 'test'
app.config['db.port'] = 27017
iweb = iWeb(app)

class TestController(APIController):

    def process(self):
        return list(self.db.test_db.find())

class TestInsertController(APIController):

    def process(self):
        param = self.get_parameters(['name', 'sur'])
        self.db.test_db.insert(param)

simple.add_url_rule(app_name+'/list', view_func=TestController.as_view('test'))
simple.add_url_rule(app_name+'/insert', view_func=TestInsertController.as_view('insert'))