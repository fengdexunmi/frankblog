# coding=utf8

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.models import Post
from django.http import Http404


# Create your views here.
# 主页
def main(request):
    posts = Post.objects.all().order_by("-create_time")
    paginator = Paginator(posts, 10)  # 每页显示10条

    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator._num_pages)

    #  return render_to_response("list.html", {"posts": posts, "user": request.user})
    return render_to_response("list.html", {"posts": posts, "user": request.user})


# add by frank at 2014.1.15 begin #
# 显示文章
def show_post(request, pid):
    try:
        post = Post.objects.select_related().get(id=int(pid))
    except:
        raise Http404

    return render_to_response("post.html", {"post": post})
