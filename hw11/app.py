from flask import Flask
from views import views, showme
from database import db


def create_app():
    app = Flask(__name__)
    app.config.update({
        'DEBUG': True,
        'DEFAULT_RESPONSE': 'It\'s my first fabric',
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///blog.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    })
    app.register_blueprint(views)
    app.register_blueprint(showme)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
