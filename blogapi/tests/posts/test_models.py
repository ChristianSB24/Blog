import pytest

from posts.models import Post
from posts.models import CustomUser


@pytest.mark.django_db
def test_post_model():
    testuser1 = CustomUser.objects.create_user(username='testuser1', password='abc123')
    testuser1.save()
    post = Post.objects.create(
    	author=testuser1, title="Learning to Code", entry="Today I programmed Hello")
    post.save()

    assert post.author ==testuser1
    assert post.title == "Learning to Code"
    assert post.entry == "Today I programmed Hello"
    assert post.created_at
    assert post.updated_at
    assert str(post) == post.title