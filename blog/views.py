from django.shortcuts import render
# from .models import Post, Comment
# # Create your views here.

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = post.comment_set.all()
#     return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

# def comment_create(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == 'POST':
#         comment = Comment.objects.create(post = post, content = request.POST['content'])
#         return render(request, 'blog/post_detail.html', {'post': post, 'comments': comment})
#     return render(request, 'blog/comment_create.html')


def home(request):
    return render(request, 'home.html', {})