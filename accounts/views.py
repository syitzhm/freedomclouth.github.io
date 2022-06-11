from urllib import response

import django.views.generic as Listview
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from accounts.forms import ProfileForm,Testform
from accounts.forms import TestModelform, ProfileForm
from django.contrib import messages
from django.views.generic import TemplateView,ListView

from accounts.models import Ouser
from customize.models import Category, Quotation
import os
# Create your views here.

@login_required
def profile_view(request):
    return render(request,'account/profile.html')


def dashboard(request):
    return render(request,'account/dashboard.html')

def dashboardn(request):
    quotationlist= Quotation.objects.all()
    context = {'quotationlist':quotationlist}
    return render(request,'account/dashboard_n.html',context)

class test(ListView):
    model = Category
    form_class= TestModelform
    template_name = "order/account.html"
    # context_object_name = {'form':form }

def test_json(request):
    quotations = Quotation.objects.all()
    data= [quotation.get_data() for quotation in quotations]
    response = {'data' : data}
    return JsonResponse(response)


@login_required
def change_profile_view(request):
    if request.method == 'POST':
        old_avatar_file = request.user.avatar.path
        old_avatar_url = request.user.avatar.url
        # 上传文件需要使用request.FILES
        form = ProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            if not old_avatar_url == '/media/avatar/default.png':
                if os.path.exists(old_avatar_file):
                    os.remove(old_avatar_file)
            form.save()
            # 添加一条信息,表单验证成功就重定向到个人信息页面
            messages.add_message(request,messages.SUCCESS,'个人信息更新成功！')
            return redirect('accounts:profile')
    else:
        # 不是POST请求就返回空表单
        form = ProfileForm(instance=request.user)
    return render(request,'account/change_profile.html',context={'form':form})

