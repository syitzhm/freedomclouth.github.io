from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic
from .models import mainclouth


# def Index(request):
#     return render(request,'../templates/common/index.html')
    # model = Timeline
    # template_name = '../templates/common/index.html'
    # context_object_name = 'timeline_list'
    #
class Index(generic.ListView):
    model=mainclouth
    template_name = 'common/index.html'
    context_object_name = 'mainclouths'

    def get_queryset(self):  # 重写get_queryset方法
        # 获取所有is_main为True的clouth，并且以时间倒序返回数据
        return mainclouth.objects.filter(is_main= True).order_by('-create_date')

def Single(request):
    return render(request,'common/single.html')
    # model = Timeline
    # template_name = '../templates/common/index.html'
    # context_object_name = 'timeline_list'


def Products(request):
    return render(request,'common/products.html')