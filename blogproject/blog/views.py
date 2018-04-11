
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Port,Category
import markdown
from comments.forms import CommentForm
# from django.views.generic import ListView
from django.views.generic import ListView,DetailView
# Create your views here.

# 首页数据
class IndexView(ListView):
    model = Port
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    # 指定每一页的数据  实现自动分页
    paginate_by = 10

# 详情页视图
def detail(request,pk):
    port = get_object_or_404(Port,pk=pk)

    # 阅读量+1
    port.increase_views()

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

class PortDetailView(DetailView):
    model = Port
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):

        response = super(PortDetailView,self).get(*args,**kwargs)
        self.object.increase_views()

        return response


    def get_object(self, queryset=None):
        post = super(PortDetailView,self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PortDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context

# 归档视图函数

class ArchivesView(ListView):
    model = Port
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month=self.kwargs.get('month')
        return super(Archives,self).get_queryset().filter(created_time__year=year,
                                                          created_time__month=month)
# def archives(request,year,month):
#     port_list = Port.objects.filter(created_time__year=year,
#                                     created_time__month=month
#                                     ).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'port_list': port_list})


# 分类视图函数
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Port.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


class categoryView(ListView):
    model = Port
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(categoryView,self).get_queryset().filter(category=cate)



