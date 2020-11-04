from datetime import datetime
from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"

'''
# To actually create de db:
python
from flaskblog import db
from flaskblog.models import User, Post
db.create_all()

# To create data
user_1 = User(username='Bruno', email='bruno99sr@gmail.com', password='password1') #id is added auto
db.session.add(user_1) # need to be commited
user_2 = User(username='Bruno2', email='bruno@demo.com', password='password2')
db.session.add(user_2)
db.session.commit()

# Querying the db
User.query.all() # returns list of all users
User.query.first()
User.query.filter_by(Username='Bruno).all()
User.query.filter_by(Username='Bruno).first()
user = User.query.filter_by(Username='Bruno).first()
user
user.id
user = User.query.get(1)
user.posts

# Creating posts
post_1 = Post(title='blog1', content='first post content', user_id=user.id)
post_2 = Post(title='blog2', content='scnd post content', user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()

# Looking at posts
user.posts # return list
for post in user.posts:
    print(post.title)
post = Post.query.first()
post.user_id
post.author

# Clear data
db.drop_all()
db.create_all()

'''