# coding=utf8
from django.contrib.auth.models import User
from django.db import models
from markdown import markdown


# Create your models here.
# 标签模型
# add by frank at 2014.1.16 begin #
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='标签')

    def __unicode__(self):
        return self.name

    def get_tag_url(self):
        return '/tag/%s' % self.name

    class Meta:
        verbose_name_plural = '标签'

# add by frank at 2014.1.16 end #


class Category(models.Model):
    """
    分类 是一个树型结构
    add by frank at 2014.2.7
    """
    name = models.CharField(max_length=30, blank=False, unique=True, verbose_name='分类(子节点)')
    parent = models.ForeignKey('self', related_name='categories', blank=True, null=True, verbose_name='分类(根节点)')

    def __unicode__(self):
        return self.name

    def get_category_url(self):
        if self.parent:
            return '/category/%s' % self.name
        else:
            return '/%s' % self.name

    class Meta:
        verbose_name_plural = '分类'


class Post(models.Model):
    STATUS_CHOICES = (
        (1, '草稿'),
        (2, '发布'),
    )  # 文章状态二元元组 add by frank at 2014.2.10
    title = models.CharField(max_length=60, verbose_name='标题')  # 文章标题
    author = models.ForeignKey(User, verbose_name='作者')  # 作者
    slug = models.CharField(max_length=50, blank=True, null=True, db_index=True, verbose_name='文章链接',
                            help_text='可包含字母、数字、连字符、下划线')  # 文章链接
    tags = models.ManyToManyField(Tag, null=True, verbose_name='标签')  # 标签 add by frank at 2014.1.16
    category = models.ForeignKey(Category, verbose_name='分类')  # 分类 add by frank at 2014.2.7
    content = models.TextField(verbose_name='内容')  # 文章内容
    create_time = models.DateTimeField(auto_now_add=True)  # auto_now_add是对象第一次被创建的时间
    modify_time = models.DateTimeField(auto_now=True)  # 修改、编辑时间=发布时间 add at 2014.2.10
    status = models.IntegerField(choices=STATUS_CHOICES, default=2, verbose_name='状态')  # 文章状态 add 2014.2.10
    content_html = models.TextField(editable=False, blank=True)  # 添加markdown支持,add by frank at 2014.1.23

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%s/%s' % (self.id, self.slug)

    # # add by frank at 2014.1.18 begin #
    # # 当前文章的前一篇文章的绝对地址
    # def get_previous_url(self):
    #     post = self.get_previous_by_create_time()
    #     return post.get_absolute_url()
    #
    # # 当前文章的前一篇文章的绝对地址
    # def get_next_url(self):
    #     post = self.get_next_by_create_time()
    #     return post.get_absolute_url()
    #
    # def get_previous_title(self):
    #     post = self.get_previous_by_create_time()
    #     return post.title
    #
    # def get_next_title(self):
    #     post = self.get_next_by_create_time()
    #     return post.title
    # # add by frank at 2014.1.18 end #

    def get_previous_post(self):
        return self.get_previous_by_modify_time(status=2)

    def get_next_post(self):
        return self.get_next_by_modify_time(status=2)

    # add by frank at 2014.1.23 begin #
    # 添加markdown语法支持
    def save(self, force_insert=False, force_update=False):
        self.content_html = markdown(self.content)
        super(Post, self).save(force_insert, force_update)
    # add by frank at 2014.1.23 end #

    class Meta:
        verbose_name_plural = '文章'