from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User, Post, Profile
import json
from rest_framework import generics
from .serializers import PostSerializer


# serializer Post
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('id')
#     serializer_class = PostSerializer


# class PostView(generics.CreateAPIView):
class PostView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer


def newpost(request):
    if request.method == 'POST':
        # text = str(request.POST.get('post'))
        post = Post(text=str(request.POST.get('post')), user=request.user)
        # post.text = str(request.POST.get('post'))
        # post.user = request.user
        post.save()
    return render(request, "network/index.html")


# def posts(request):
#     posts = Post.objects.all()
#     p = Paginator(posts, 10)
#     start = int(request.GET.get('start') or 0)
#     end = int(request.GET.get('end') or start + 9)
#     if end > len(posts):
#         end = len(posts)
#     # data = [f'Post #{i}' for i in range(start, end, 1)]
#     data = []
#     for i in range(start, end, 1):
#         # get the posts from the model
#         data.append({
#             'user': {posts[i].user},
#             'text': {posts[i].text},
#             'date': {posts[i].date},
#             'likes': {posts[i].likes}
#         })
#         # data.append(f'Post #{i} {posts[i].text} by {posts[i].user}')
#
#     return JsonResponse({"posts": json.dumps(str(data))})


def index(request):
    # data = posts(request)
    data = str(Post.objects.all())
    if request.method == "POST":
        if request.user.is_authenticated():
            postform = PostForm
            # postform = PostForm(data=request.POST)
            return render(request, "network/index.html", {'user': request.user, 'post': data})
    else:
        return render(request, "network/index.html", {'post': data})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        profile = Profile(user=user)
        profile.save()
        print(f'created {profile}')
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profile(request, username):
    user_posts = Post.objects.filter(user=username).order_by('-date')
    posts = []
    for i in range(len(user_posts)):
        posts.append({'date': user_posts[i].date.strftime('%H:%M %d %b %Y'), 'text': user_posts[i].text,
                      'likes': len(user_posts[i].likes.all())})
    status = request.user.is_authenticated
    ###el profile que se esta visitando
    user = User.objects.get(username=username)
    # profile = Profile.objects.get(user=user)
    ###el usuario q esta haciendo el requiest
    user_profile = Profile.objects.get(user=request.user)
    ### folling a user el que hace el request
    # user_profile.following.add(user) #funcionando migue folling leo
    following_status = user in user_profile.following.all()
    # print(f'{user_profile} following {user}: {user in user_profile.following.all()}')
    followers = 0
    for u in Profile.objects.all():
        if user in u.following.all():
            followers += 1
    return JsonResponse({'followers': followers,
                         'posts': posts,
                         'logged': status,
                         'following_status': following_status,
                         'request_user': str(request.user)
                         })


@login_required
@csrf_exempt
def follow(request, username):
    # print(username)
    if request.method != 'POST':
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    # print(f'data= {data}')
    follow = data.get("follow")
    # print(f'follow= {follow}')
    #procedimiento para seguir al usuario para
    user = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=request.user)
    if not follow:
        user_profile.following.add(user)
        # print(f'{user_profile} following {user}')
        user_profile.save()
        return JsonResponse({'status': 201, 'action': "Follow"})
    #procedimeinto para dejar de seguir
    elif follow:
        user_profile.following.remove(user)
        # print(f'{user_profile} unfollowing {user}')
        user_profile.save()
        return JsonResponse({'status': 201, 'action': "Unfollow"})
    return JsonResponse({}, status=404)


@login_required
@csrf_exempt
def following_posts(request):
    all_posts = Post.objects.order_by('-date').all()
    user = Profile.objects.get(user=request.user)
    following_users = user.following.all()

    fpost = {}
    for user in following_users:
        for post in all_posts:
            if post.user == user:
                # print(len(post.likes))
                # TODO: ver el comportamiento de la variable like cuando tenga mas likes
                likes = post.likes.count()
                # print(likes)
                if str(user) in fpost:
                    fpost[str(user)].append({'id': post.id, 'text': post.text, 'date': post.date, 'likes': likes})
                else:
                    fpost[str(user)] = [{'id': post.id, 'text': post.text, 'date': post.date, 'likes': likes}]
    return JsonResponse({'status': 201, 'post': fpost})


def user_requesting(request):
    user = None
    if str(request.user) != 'AnonymousUser':
        user = str(request.user)
    return JsonResponse({'user_requesting': user})


@login_required
@csrf_exempt
def edit_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get("id")
        post = Post.objects.get(id=post_id)
        post.text = data.get('text') + ' (edited)'
        post.save()
        return JsonResponse({'status': 201})


@login_required
@csrf_exempt
def like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)
        post_id = data.get("id")
        post = Post.objects.get(id=post_id)
        user = User.objects.get(username=request.user)
        liked = True
        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
            # print(f'{user} dont like')
        else:
            post.likes.add(user)
            # print(f'{user} likes')
        post.save()
        likes = post.likes.count()
        return JsonResponse({'status': 201, 'liked': liked, 'likes': likes})


@login_required
@csrf_exempt
def like_status(request):
    # print('requesting like status')
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get("id")
        # print(post_id)
        post = Post.objects.get(id=post_id)
        user = User.objects.get(username=request.user)
        liked = False
        if user in post.likes.all():
            liked = True
        return JsonResponse({'status': 201, 'liked': liked})
