from app.db import db

class Income(db.Model):
    __tablename__ = 'incomes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=False)
    wallet = db.Column(db.String, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "wallet": self.wallet,
        }
