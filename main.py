from flask import Flask, jsonify
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


@app.route('/')
def home():
    users = User.query.all()
    print(users)
    return "jsonify(users)"


@app.route('/api/')
def test_api():
    videos = Video.query.limit(10).all()
    print(55555, videos)
    return jsonify({'a': 1, 'b': 2})


class User(db.Model):

    __tablename__ = 'user_table_name'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User00 `{}`>".format(self.username)


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    img_src = db.Column(db.Text())
    video_addr = db.Column(db.Text())
    director = db.Column(db.String(255))
    performer = db.Column(db.String(255))
    language = db.Column(db.String(255))
    classify = db.Column(db.String(255))
    area = db.Column(db.String(255))

    status = db.Column(db.Integer())
    up_date = db.Column(db.String(255))
    release_date = db.Column(db.String(255))
    introduce = db.Column(db.Text())
    is_free = db.Column(db.Integer())
    is_vip = db.Column(db.Integer())
    is_eg = db.Column(db.Integer())

    def __init__(self, img_src):
        self.img_src = img_src

    def __repr__(self):
        return "<Videos_img_src `{}`>".format(self.img_src)


if __name__ == "__main__":
    app.run()
