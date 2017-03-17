from wtforms_alchemy import ModelForm
from models import Post, Tag, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'author_id'
        ]


class TagForm(ModelForm):
    class Meta:
        model = Tag


class UserForm(ModelForm):
    class Meta:
        model = User
