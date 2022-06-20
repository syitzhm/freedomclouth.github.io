import json
import random
import time


import markdown
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView
from markdown.extensions.toc import TocExtension
from .addquotation import addQuotation


import common.models
import customize.models
from customize.models import Quotation, Category,Quoinprog,tempQuotation
from accounts.models import Ouser
from customize.forms import save_quotation_form, save_quofeedback_form
from django.contrib import messages
import os
# Create your views here.

def slugstr():
    slugstrn = int(time.time())+random.randint(0, 10000)
    return slugstrn

@login_required
def QuotationListView(request):
    quotationlist = Quotation.objects.filter(is_open=True,is_assigned=False)
    myquotationlist = Quoinprog.objects.filter(rep_id=request.user.id)
    # print("quotationlist",quotationlist)
    context = {'quotationlist': quotationlist,
               'myquotationlist': myquotationlist}
    return render(request,'customize/quotationlist.html', context)

@login_required
def MyQuotationListView(request):
    print("-=-=-=-=>request id", request.user.id)
    quotationlist = Quotation.objects.filter(is_open=True, is_assigned=False)
    myquotationlist = Quoinprog.objects.filter(rep_id=request.user.id)
    # print("quotationlist",quotationlist)
    context = {'quotationlist': quotationlist,
               'myquotationlist': myquotationlist}
    return render(request,'customize/myquotationlist.html', context)

@login_required
def QuoListDetailView(request,slug):
    quotationdetail = Quotation.objects.filter(quotation_id=slug)
    quoinprog=Quoinprog.objects.filter(quotation_id= Quotation.objects.filter(quotation_id=slug).first().id)
    context = {'quotationdetail': quotationdetail,
               'quoinprog':quoinprog
               }
    return render(request,'customize/quotationdetail.html', context)

@login_required
def quofeedback_detail(request,slug):
    quotationdetail = Quotation.objects.filter(quotation_id=slug)
    quoinprog=Quoinprog.objects.filter(quotation_id=slug)
    # Customername=Ouser.objects.filter(id=quotationdetail.customerid)
    print("quotationlist",quoinprog)

    context = {'quotationdetail': quotationdetail,
               'quoinprog':quoinprog
               }
    return render(request,'customize/quofeedback_detail.html', context)



def quotation_add(request):
    categorylist = Category.objects.filter(category_name="categoryA")
    print("categorylist",categorylist)

    newquotation=addQuotation(request)
    # newquotation.clear()
    # cartmaster = get_object_or_404(Cartmaster, cart_id=checkedlist)

    if request.method == "POST":
        formsleeve = str(request.POST['sleeve'])
        formsize= str(request.POST['size'])
        formgender= str(request.POST['gender'])
        formcolor = str(request.POST['color'])
        formpartnum=str(request.POST['imagelist'])
        formquantity = request.POST['quantity']
        formimages = request.FILES['images']
        # formimages = str(request.POST['images'])
        formdescription = str(request.POST['description'])
        # print("_++_+_+_+_+_+:",formimages.image.name)
        category = get_object_or_404(Category, category_name='categoryA')
        newquotation.add(category, sleeve=formsleeve, size=formsize, gender=formgender, color=formcolor,
                         imagelist=formpartnum, quantity=formquantity, images="", description=formdescription)

    print("_++_+_+_+_+_+:", newquotation.newquotation.values())
    # print("_++_+_+_+_+_+:", newquotation.newquotation.keys())
    # total_price = cart.get_total_price()
    context = {'newquotation': newquotation.newquotation.values(),
               'catelist': categorylist,}
    return render(request,'customize/newquotation.html',context)

@login_required
def addNewQuotation(request,category):
    model = customize.models.Category
    newquotation = addQuotation(request)
    categorylist = Category.objects.filter(category_name=category)
    tempQuotationlist = tempQuotation.objects.filter(customer_id=request.user.id)
    print("categorylist",categorylist,newquotation)
    context = {'catelist': categorylist,
               'newquotation':newquotation.newquotation.values(),
               'catename':category,
               'tempQuotationlist':tempQuotationlist
               }
    return render(request,'customize/newquotation.html', context)

@login_required
def CustomizeView(request,slug):
    categorylist = Category.objects.filter(category_name=slug)
    tempQuotationlist=tempQuotation.objects.filter(customer_id=request.user.id)
    print("categorylist",categorylist)
    context = {'catelist': categorylist,
               'catename': slug,
               'tempQuotationlist':tempQuotationlist}
    return render(request,'customize/customize.html', context)

class QuoinprogView(generic.ListView):
    model = Quoinprog
    template_name = 'customize/quotationdetail.html'

    # def get_queryset(self, **kwargs):
    #     queryset = super(CustomizeView, self).get_queryset()
    #     # return queryset.filter(categoryid=slug)
    #     return queryset.filter(categoryname=self.kwargs.get('categoryid'))

@login_required
def SaveQuotation(request,slug):
    categoryname=slug
    ouser_name=Ouser.objects.get(id=request.user.id)
    checkedlist = request.POST.getlist('savetoquotation')

    newquotation = addQuotation(request)
    print("=========> checkedlist", checkedlist)
    catelist = Category.objects.get(category_name=slug)
    # print("catelist", quotationlist)
    catelistid= slug
    # print("catelistid", catelist.category_id)
    quotationid = slugstr()
    if request.method=="POST":

        for items in checkedlist:
            print("----->debuging2 %s " % (newquotation.newquotation[items]))
            execstr = Quotation.objects.create(quotation_id=quotationid,
                                               sleeve = newquotation.newquotation[items]['sleeve'],
                                               color=newquotation.newquotation[items]['color'],
                                               size=newquotation.newquotation[items]['size'],
                                               req_image="",
                                               gender=newquotation.newquotation[items]['gender'],
                                               part_number=newquotation.newquotation[items]['imagelist'],
                                               quantity=int(newquotation.newquotation[items]['quantity']),
                                               description=newquotation.newquotation[items]['description'],
                                               category_name=catelist,
                                               customer_id = ouser_name,
                                               )
            execstr.save()


        return redirect("common:index",slug=categoryname)
    else:
        save_quotation = save_quotation_form()
        context = { 'save_quotation':save_quotation,
                    'catelist':catelistid,}
        return render(request,'customize/customize.html', context)

@login_required
def SavetempQuotation(request,slug):
    ouser_name=Ouser.objects.get(id=request.user.id)
    checkedlist = request.POST.getlist('savetoquotation')

    newquotation = addQuotation(request)
    print("=========> checkedlist", checkedlist)
    catelist = Category.objects.get(category_name=slug)
    # print("catelist", quotationlist)
    catelistid= slug
    catename=slug
    print("<><><><><><><>catelistid", str(slug))
    quotationid = slugstr()
    if request.method=="POST":

        # for items in checkedlist:
        print("----->debuging2 %s " % (request.POST))
        execstr = tempQuotation.objects.create(quotation_id=quotationid,
                                                             sleeve = request.POST['sleeve'],
                                                             color=request.POST['color'],
                                                             size=request.POST['size'],
                                                             req_image=request.FILES['images'],
                                                             gender=request.POST['gender'],
                                                             part_number=request.POST['imagelist'],
                                                             quantity=int(request.POST['quantity']),
                                                             description=request.POST['description'],
                                                             category_name=catelist,
                                                             customer_id = ouser_name,
                                                             )
        execstr.save()
        tempQuotationlist = tempQuotation.objects.all()

        return redirect("customize:addnewquotation",category=catelistid)
    else:
        save_quotation = save_quotation_form()
        context = { 'save_quotation':save_quotation,
                    'catelist':catelistid,
                    'catename':catename,
                    }
        return render(request,'customize/customize.html', context)


@login_required
def SaveQuoFeedback(request,slug):
    quotationlist = int(Quotation.objects.get(quotation_id=slug).quotation_id)
    ouser_name = Ouser.objects.get(id=request.user.id)
    print("quotationlist",type(quotationlist),quotationlist)
    # quoinprog = Quoinprog.objects.all()
    # catelist = Category.objects.filter(categoryid=slug).first()
    # print("catelist", catelist)
    # catelistid= slug
    # print("catelistid", catelistid)
    quotation_id = slugstr()
    if request.method=="POST":
        save_quotation = save_quofeedback_form(data=request.POST)
        print("----->debuging %s " % (save_quotation.is_valid()))
        if save_quotation.is_valid():
            new_Quotation = save_quotation.save(commit=False)
            # categoryid = Category.objects.get(id=request.POST['category'])
            # print("----->debuging %s " % (request.FILES.getlist('images')))


            # quotationlist = Quotation.objects.get(quotationid=quotationlist.quotationid)
            quotationlist= Quotation.objects.get(quotation_id=slug)
            # print("quotationlist",type(quotationlist))

            execstr = Quoinprog.objects.create(quotation_id=quotationlist,
                                               feedback_image=request.FILES.get('images'),
                                               rep_id=ouser_name,
                                               desc_feedback=request.POST['desc_feedback'])
            execstr.save()

            quotationlist.is_assigned =True
            quotationlist.save()
            return redirect("common:index")
        else:
            print(save_quotation.errors)
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        save_quotation = save_quofeedback_form()
        context = { 'save_quotation':save_quotation,
                    # 'quotationlist': quotationlist,
                    }
        return render(request,'../templates/customize/customize.html', context)


