from app import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100)) 
    date = db.Column(db.String(100)) 
    place = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<ID of the location column is {self.id}>' 
    