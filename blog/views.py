# coding=utf8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.models import Post, Tag, Category
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# 主页
def main(request):
    posts = Post.objects.filter(status=2).order_by("-modify_time")
    paginator = Paginator(posts, 3)  # 每页显示10条

    tags = Tag.objects.all()

    category_root = Category.objects.filter(parent=None)  # 获取分类的根节点

    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("home.html", {"posts": posts, "tags": tags, "category_root_list": category_root})


# add by frank at 2014.1.15 begin #
# 显示文章
def show_post(request, pid):
    try:
        post = Post.objects.select_related().get(id=int(pid))
        tags_by_post = post.tags.all()
        tags_all = Tag.objects.all()
        categories = Category.objects.filter(parent=None)
    except:
        raise Http404

    return render_to_response("blog_post.html",
                              {
                                  "post": post,
                                  "tags_by_post": tags_by_post,
                                  "tags": tags_all,
                                  "category_root_list": categories
                              },
                              context_instance=RequestContext(request))

# add by frank at 2014.1.15 end #


# add by frank at 2014.1.16 begin #
# 根据标签显示相关文章
def list_post_by_tag(request, tag):
    try:
        posts_by_tag = Post.objects.filter(status=2).filter(tags__name=tag)  # 根据ManyToMany字段查找相关的数据
        # tag_obj = Tag.objects.get(name=tag)
        # posts_by_tag = tag_obj.post_set
        tags = Tag.objects.all()
        categories = Category.objects.filter(parent=None)
    except:
        raise Http404

    paginator = Paginator(posts_by_tag, 3)  # 每页显示3条

    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1

    try:
        posts_by_tag = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_by_tag = paginator.page(paginator.num_pages)

    return render_to_response("home.html",
                              {
                                  "posts": posts_by_tag,
                                  "selected_tag": tag, "tags": tags,
                                  "category_root_list": categories
                              })

# add by frank at 2014.1.16 #


def list_post_by_category(request, category):
    try:
        posts_by_category = Post.objects.filter(status=2).filter(category__name=category)
        Category.objects.get(name=category)
    except ObjectDoesNotExist:
        raise Http404

    paginator = Paginator(posts_by_category, 3)
    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1
    try:
        posts_by_category = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_by_category = paginator.page(paginator.num_pages)

    tags = Tag.objects.all()
    categories = Category.objects.filter(parent=None)

    return render_to_response("home.html",
                              {
                                  "posts": posts_by_category,
                                  "selected_category": category,
                                  "tags": tags,
                                  "category_root_list": categories
                              })


def list_post_by_root(request, root):
    try:
        posts_by_root = Post.objects.filter(status=2).filter(category__parent__name=root)
        Category.objects.get(name=root)
    except ObjectDoesNotExist:
        raise Http404

    paginator = Paginator(posts_by_root, 3)
    try:
        page = int(request.GET.get("page", "1"))
    except ValueError:
        page = 1
    try:
        posts_by_root = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_by_root = paginator.page(paginator.num_pages)

    tags = Tag.objects.all()
    categories = Category.objects.filter(parent=None)

    return render_to_response("home.html",
                              {
                                  "posts": posts_by_root,
                                  "selected_category": root,
                                  "tags": tags,
                                  "category_root_list": categories
                              })
