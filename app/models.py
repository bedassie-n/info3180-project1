from . import db

class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    # __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(1024))
    rooms = db.Column(db.String(3))
    bathrooms = db.Column(db.String(3))
    price = db.Column(db.String(50))
    ptype = db.Column(db.String(30))
    location = db.Column(db.String(4096))
    photo = db.Column(db.String(255))

    def __init__(self, title, description, rooms, bathrooms, price, ptype, location, photo):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.ptype = ptype
        self.location = location
        self.photo = photo

    def __repr__(self):
        return '<Property %r, $%r>' % (self.title, self.price)
