from turtle import title
from flask import Flask
from flask_restful import marshal,Resource,Api,reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.sqlite'
app.config['SECRET_KEY'] = 'jamesd'
db=SQLAlchemy(app)
api=Api(app)
class User(db.Model):
    username = db.Column(db.String(32),nullable=False)
    email = db.Column(db.String(32),nullable=False)
    password = db.Column(db.String(64))
    def __repr__(self):
        return f"{self.username}, {self.email}"
class Post(db.Model):
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
parser  = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)

class UserApi(Resource):
    def get(self):
        pass
    def post(self):
         args = parser.parse_args()
         username=args['username']
         email=args['email']
         password=args['password']
         user=User(username=username,email=email,password=password)
         db.session.add(user)
         db.session.commit()
#register api
api.add_resource(UserApi, '/user/details')
class Post(Resource):
    def get(self):
        pass
    def post(self):
         args = parser.parse_args()
         title=args['title']
         date_posted=args['date_posted']
         content=args['content']
         post=Post(title=title,date_posted=date_posted,content=content)
         db.session.add(post)
         db.session.commit()
#create post api
api.add_resource(UserApi, '/user/posts')
if __name__==' __main__':
    app.run(debug=True)


        
        

