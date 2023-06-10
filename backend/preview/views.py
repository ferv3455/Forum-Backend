from django.shortcuts import render

from forum.models import Post
from forum.serializers import PostFullSerializer


# Create your views here.
def preview(request, id):
    post = Post.objects.get(id=id)
    result = PostFullSerializer(post).data
    result['user_profile']['avatar'] = 'data:image/jpg;base64,' + result['user_profile']['avatar']
    images = result['images']
    for image in images:
        image['content'] = 'data:image/jpg;base64,' + image['content']
    return render(request, 'post.html', result)
