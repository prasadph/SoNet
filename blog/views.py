from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PostForm, CommentsForm
from .models import Post, Tag


def post_list(request):
    # messages.add_message(request, messages.INFO, 'Hello world.')
    email = request.user.email
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'email': email,
        # 'messages': messages,
        'posts': posts,
    })


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return render(request, 'blog/post_list.html', {})
            else:
                pass
                # Return a 'disabled account' error message

        else:
            # Return an 'invalid login' error message.
            pass
    else:
        return render(request, 'login.html', {})


def post(request):
    if request.user.is_authenticated():

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post_obj = form.save(commit=False)
                post_obj.author = request.user
                post_obj.save()

                return redirect('/blog/view/{0}'.format(post_obj.pk))
            pass
        else:
            form = PostForm()

            return render(request, 'post.html', {'form': form})
    else:
        pass


def view_post(request, post_id):
    if request.user.is_authenticated():
        form = CommentsForm(request.POST)

        post_obj = Post.objects.get(pk=post_id)
        tags = post_obj.get_tags()
        if request.method == 'POST':
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post_obj
                comment.author = request.user
                comment.save()
        comments = post_obj.get_comments()

        return render(request, 'blog/view_post.html', {
            'post': post_obj,
            'comments': comments,
            'form': form,
            'tags': tags}
        )


def posts_by_tag_id(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)

    return render(request, "tags/view.html", {
        'tag': tag,
    })
