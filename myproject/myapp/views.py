from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import User, Product, Order

from flask import render_template

logger = logging.getLogger(__name__)

# Create your views here.
"""
def main(request):
    logger.info("main was opened")
    return HttpResponse("Это главная страница. Чтобы увидеть информацию про меня перейдите в /about/.")
    #return render(request, "main.html")

def about(request):
    logger.info("about was opened")
    return HttpResponse("Это страница про меня")
"""

def main(request):
    logger.info("main was opened")
    return render(request, "myapp/main.html")

def about(request):
    logger.info("about was opened")
    return render(request, "myapp/about.html")
"""
def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
"""
def get_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'myapp/get_user.html', {'user': user})

def get_all_users(request):
    users = get_list_or_404(User)
    return render(request, 'myapp/get_all_users.html', {'users': users})

def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(user=user).order_by('id')[:5]
    return render(request, 'myapp/user_orders.html', {'user':user, 'orders': orders})

def order_full(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'myapp/order_full.html', {'order': order})

def get_user_Moscow(request):
    users = get_list_or_404(User, adress="г. Москва")
    return render(request, 'myapp/get_user_Moscow.html', {'users': users})

def get_user_Saint_Petersburg(request):
    users = get_list_or_404(User, adress="г. Санкт-Петербург")
    return render(request, 'myapp/get_user_Saint_Petersburg.html', {'users': users})


