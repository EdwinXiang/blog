from django.contrib.syndication.views import Feed
from .models import Port

class AllPortRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Django 博客教程演示项目"

    # 通过聚合阅读器跳转到网站的地址
    link = "/"

    # 显示在聚合阅读器上的描述信息
    description = "Django 博客教程演示项目测试文章"

    def items(self):
        return Port.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category,item.title)

    def item_description(self, item):
        return item.body