from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic


# def Index(request):
#     return render(request,'../templates/common/index.html')
    # model = Timeline
    # template_name = '../templates/common/index.html'
    # context_object_name = 'timeline_list'
    #
class Index(generic.TemplateView):
    template_name = 'common/index.html'

def Single(request):
    return render(request,'common/single.html')
    # model = Timeline
    # template_name = '../templates/common/index.html'
    # context_object_name = 'timeline_list'


def Products(request):
    return render(request,'common/products.html')