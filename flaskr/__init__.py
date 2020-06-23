import os
import time
from flask import Flask, g, jsonify, abort, request
from flask_babelex import Babel
# from flask_user import current_user, login_required, roles_required, UserManager, UserMixin


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return {'name': 'Hello, Karla!'}

    @app.route('/time')
    def get_current_time():
        return {'time': time.time()}

    @app.route('/test')
    def test():
        return {'a': 39} 
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import userspace
    app.register_blueprint(userspace.bp)

    return app