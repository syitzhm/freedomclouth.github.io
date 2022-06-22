from datetime import datetime
from urllib import response

import django.views.generic as Listview
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from accounts.forms import ProfileForm,Testform
from django.views.decorators.http import require_POST

from accounts.forms import TestModelform, ProfileForm
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.decorators.csrf import csrf_protect

from accounts.models import Ouser,Notification
from customize.models import Category, Quotation
from order.models import Ordermaster
from order.forms import save_order_form
import os
from accounts.templatetags import comment_tags
# Create your views here.

@login_required
def profile_view(request):
    quotation = Quotation.objects.filter(customer_id=request.user.id)
    ordermaster = Ordermaster.objects.filter(customer_id=request.user.id)
    context= {'quotation':quotation,
              'ordermaster':ordermaster}
    return render(request,'account/profile.html',context)


def dashboard(request):
    return render(request,'account/dashboard.html')

def dashboardn(request):
    quotationlist= Quotation.objects.all()
    context = {'quotationlist':quotationlist}
    return render(request,'account/dashboard_n.html',context)

def test(request):
    notification= Notification.objects.all()
    context= {'notification':notification}
    return render(request,'account/notification.html',context)

def test_json(request):
    quotations = Quotation.objects.all()
    data= [quotation.get_data() for quotation in quotations]
    response = {'data' : data}
    return JsonResponse(response)

@login_required
def NotificationView(request, is_read=None):
    '''展示提示消息列表'''
    now_date = datetime.now()
    return render(request, 'account/notification.html', context={'is_read': is_read, 'now_date': now_date})

@login_required
@csrf_protect
def change_profile_view(request):
    print("inside change profile view")
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

@login_required
@csrf_protect
def change_avatar(request):
   avatar = Ouser.objects.get(pk=request.user.id)
   print("inside avatar save",avatar.avatar)
   if request.method == "POST":
       avatar.avatar = request.FILES['avatar']
       avatar.save()

   return redirect("accounts:profile")

# user_model = settings.AUTH_USER_MODEL


# @login_required
# @require_POST
# def AddcommentView(request):
#     if request.is_ajax() and request.method == "POST":
#         data = request.POST
#         new_user = request.user
#         new_content = data.get('content')
#         article_id = data.get('article_id')
#         rep_id = data.get('rep_id')
#         the_article = Article.objects.get(id=article_id)
#         if len(new_content) > 1048:
#             return JsonResponse({'msg': '你的评论字数超过1048，无法保存。'})
#
#         if not rep_id:
#             new_comment = ArticleComment(author=new_user, content=new_content, belong=the_article, parent=None,
#                                          rep_to=None)
#         else:
#             new_rep_to = ArticleComment.objects.get(id=rep_id)
#             new_parent = new_rep_to.parent if new_rep_to.parent else new_rep_to
#             new_comment = ArticleComment(author=new_user, content=new_content, belong=the_article, parent=new_parent,
#                                          rep_to=new_rep_to)
#         new_comment.save()
#         new_point = '#com-' + str(new_comment.id)
#         return JsonResponse({'msg': '评论提交成功！', 'new_point': new_point})
#     return JsonResponse({'msg': '评论失败！'})





@login_required
@require_POST
def mark_to_read(request):
    '''将一个消息标记为已读'''
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        user = request.user
        id = data.get('id')
        info = get_object_or_404(Notification, get_p=user, id=id)
        info.mark_to_read()
        return JsonResponse({'msg': 'mark success'})
    return JsonResponse({'msg': 'miss'})


@login_required
@require_POST
def mark_to_delete(request):
    '''将一个消息删除'''
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        user = request.user
        id = data.get('id')
        info = get_object_or_404(Notification, get_p=user, id=id)
        info.delete()
        return JsonResponse({'msg': 'delete success'})
    return JsonResponse({'msg': 'miss'})
