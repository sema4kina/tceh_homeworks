from flask import Blueprint, request, render_template
from forms import PostForm, TagForm, UserForm
from database import db

views = Blueprint('views', __name__, url_prefix='/views', template_folder='templates')
showme = Blueprint('showme', __name__, url_prefix='/showme', template_folder='templates')


@views.route('/tag/create/', methods=['POST'])
def create_tag():
    from models import Tag
    print(request.form)
    form = TagForm(request.form)
    tag = Tag(tagname=form.tagname.data)
    db.session.add(tag)
    db.session.commit()
    return 'Tag was created!'


@views.route('/post/', methods=['POST', 'GET'])
def create_post():
    from models import Post
    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)
        post = Post(**form.data)
        db.session.add(post)
        db.session.commit()
        return 'Post was created!'
    posts = Post.query.all()
    return render_template('posts.txt', posts=posts)


@views.route('/user/create/', methods=['POST'])
def create_user():
    from models import User
    print(request.form)
    form = UserForm(request.form)
    user = User(**form.data)
    db.session.add(user)
    db.session.commit()
    return 'User was created!'


@showme.route('/visibleposts/')
def visible_posts():
    from models import Post
    posts = Post.query.filter(Post.is_visible == False).order_by(Post.date_created)
    return render_template('posts.txt', posts=posts)


@showme.route('/byslug/<slug>/')
def show_by_slug(slug):
    from models import Post
    post = Post.query.filter(Post.slugfield == slug)
    return render_template('posts.txt', posts=post)
