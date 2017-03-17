from sqlalchemy.orm import relationship
from datetime import date
from slugify import slugify
from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    posts = relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Person {} {} >'.format(self.surname, self.name)


tags = db.Table(
    'tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), primary_key=False, nullable=False)
    content = db.Column(db.String(2000), primary_key=False, nullable=False)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
        index=True
    )
    date_created = db.Column(db.Date, default=date.today())
    is_visible = db.Column(db.Boolean, default=True)
    slugfield = db.Column(db.String(300), unique=True)
    tag = relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('tags', lazy='dynamic')
    )

    def __init__(self, title, content, author_id, date_created, is_visible, slugfield):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.date_created = date_created
        self.is_visible = is_visible
        self.slugfield = slugify(self.title + '-' + str(self.date_created))

    def __repr__(self):
        return '<Post {} >'.format(self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tagname is {} >'.format(self.tagname)
