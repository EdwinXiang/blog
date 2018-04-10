
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Port,Category
import markdown
from comments.forms import CommentForm
# Create your views here.

# 首页数据
def index(request):
    post_list = Port.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

# 详情页视图
def detail(request,pk):
    port = get_object_or_404(Port,pk=pk)
    html = markdown.markdown(port.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    port.body = html
    form = CommentForm()
    comment_list = port.comment_set.all()
    context = {'post':port,
               'form':form,
               'comment_list':comment_list
               }
    return render(request,'blog/detail.html',context=context)

# 归档视图函数
def archives(request,year,month):
    port_list = Port.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'port_list': port_list})


# 分类视图函数
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Port.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})



