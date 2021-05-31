from website import db, login_manager
from flask_login import UserMixin

# this allows people to log in and register
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # username = email
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    datasets = db.relationship('Dataset', backref='author', lazy=True)
    
    def __repr__(self):
        return f"Username: {self.username}"

class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    title = db.Column(db.String(50), unique=True, nullable=False) # title given by user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # user associated with the dataset
    # some constants
    rm = db.Column(db.Float)
    o = db.Column(db.Float)
    ps = db.Column(db.Float)
    ad = db.Column(db.Float) # domain area fraction
    nd = db.Column(db.Integer) # number of domains
    status = db.Column(db.String(12), default='idle') # status = "running", "completed", "idle", etc.


