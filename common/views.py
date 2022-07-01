from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.views import generic
from django.views.decorators.http import require_POST

from accounts.models import Ouser, Notification
from customize.models import tempQuotation
from .models import mainclouth
# from customize.models import tempQuotation


# def Index(request):
#     return render(request,'../templates/common/index.html')
    # model = Timeline
    # template_name = '../templates/common/index.html'
    # context_object_name = 'timeline_list'
    #
def Index(request):
    ouser=Ouser.objects.filter(id=request.user.id)
    mainclouths= mainclouth.objects.filter(is_main=True).order_by('-create_date')
    model=mainclouth
    msgnum=Notification.objects.filter(to_user_id=request.user.id)
    print('msgnum',msgnum)
    # template_name = 'common/index.html'
    context = {'mainclouths':mainclouths,
               'msgnum':msgnum }
    return render(request, 'common/index.html', context)


def Single(request,slug):
    clouth=mainclouth.objects.filter(slug=slug)
    context = {'clouth':clouth}

    # return redirect("common:single",slug=slug)
    return render(request,'common/single.html',context)


class Products(generic.ListView):
    model = mainclouth
    template_name = 'common/products.html'
    context_object_name = 'mainclouths'

    def get_queryset(self):  # 重写get_queryset方法
        # 获取所有is_main为True的clouth，并且以时间倒序返回数据
        return mainclouth.objects.all().order_by('-create_date')

@login_required
def mark_to_delete(request,slug,categoryname):
    '''将一个消息删除'''
    print("~~~~~~~~~",request.method)
    if  request.method == "GET":
        catename =request.GET.get("categorynamea",None)
        print('catename',catename)
        user = request.user
        info = tempQuotation.objects.filter(customer_id=user.id, quotation_id=slug)
        info.delete()
        tempQuotationlist = tempQuotation.objects.filter(customer_id=user.id,is_open=True)
        context= {'tempQuotationlist':tempQuotationlist,
                  'catename':categoryname}
        return render(request,'customize/newquotation.html', context)
