from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Rate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False, index=True)
    code = db.Column(db.String(3), nullable=False, index=True)
    ammount = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return f"<Rate {self.code} on {self.date}: {self.ammount} units = {self.rate} CZK>"
    
    
