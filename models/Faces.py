from app import db 

class Face(db.Model):
    id = db.Column(db.String(50), primary_key=True, nullable=False)
    