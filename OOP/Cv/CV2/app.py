from flask import Flask

from models import db, Rate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        codes = db.session.query(Rate.code).distinct().all()
        codes = [code[0] for code in codes]
        return f"Available currency codes: {', '.join(codes)}"


    return app


if __name__ == '__main__':
    app.run(debud=True)