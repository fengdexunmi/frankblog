# coding=utf8

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.models import Post, Tag
from django.http import Http404


# Create your views here.
# 主页
def main(request):
    posts = Post.objects.all().order_by("-create_time")
    paginator = Paginator(posts, 5)  # 每页显示10条

    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    #  return render_to_response("list.html", {"posts": posts, "user": request.user})
    return render_to_response("list.html", {"posts": posts, "user": request.user})


# add by frank at 2014.1.15 begin #
# 显示文章
def show_post(request, pid):
    try:
        post = Post.objects.select_related().get(id=int(pid))
        tags = post.tags.all()
    except:
        raise Http404

    return render_to_response("post.html", {"post": post, "tags": tags})
    # return render_to_response("post.html", {"post": post})

# add by frank at 2014.1.15 end #


# add by frank at 2014.1.16 begin #
# 根据标签显示相关文章
def list_post_by_tag(request, tag):
    try:
        posts_by_tag = Post.objects.filter(tags__name=tag)  # 根据ManyToMany字段查找相关的数据
        # tag_obj = Tag.objects.get(name=tag)
        # posts_by_tag = tag_obj.post_set
    except:
        raise Http404

    paginator = Paginator(posts_by_tag, 5)  # 每页显示10条

    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1

    try:
        posts_by_tag = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_by_tag = paginator.page(paginator.num_pages)

    return render_to_response("list.html", {"posts": posts_by_tag, "tag": tag})

# add by frank at 2014.1.16 #
