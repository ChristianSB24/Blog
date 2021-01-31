import pytest
from posts.serializers import PostSerializer
from posts.models import CustomUser
from posts.models import Post


@pytest.mark.django_db
def test_valid_post_serializer():
	testuser1 = CustomUser.objects.create_user(username='testuser1', password='abc123')
	testuser1.save()
	post = Post.objects.create(
		author=testuser1, title="Learning to Code", entry="Today I programmed Hello")
	post.save()
	serializer = PostSerializer(data=post)
	assert post.author ==testuser1
	assert post.title == "Learning to Code"
	assert post.entry == "Today I programmed Hello"

def test_invalid_post_serializer():
	invalid_serializer_data = {
	    "author": "",
	    "title": "Coding",
	    "entry": "Today I coded my first line of code"
	}
	serializer = PostSerializer(data=invalid_serializer_data)
	assert not serializer.is_valid()
	assert serializer.validated_data == {}
	assert serializer.data == invalid_serializer_data
	assert serializer.errors == {"author": ["This field may not be null."]}