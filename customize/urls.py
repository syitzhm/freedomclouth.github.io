"""common URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path, include, re_path
from customize.views import \
    CustomizeView, SaveQuotation, QuotationListView, QuoListDetailView, \
    SaveQuoFeedback,quofeedback_detail,MyQuotationListView,addNewQuotation,\
    SavetempQuotation

urlpatterns = [
    path('customize/<slug:slug>/', CustomizeView, name='customize'),
    # path('customize/', CustomizeView.as_view(), name='customize'),
    # path('article/<slug:slug>/', DetailView.as_view(), name='detail'),  # 文章内容页
    path('savequotation/<slug:slug>', SaveQuotation, name='save'),
    path('savetempquotation/<slug:slug>', SavetempQuotation, name='savetempquotation'),
    # path('addquotation/', quotation_add, name='quotation_add'),
    path('quotationlist/', QuotationListView, name='quotationlist'),
    path('myquotationlist/', MyQuotationListView, name='myquotationlist'),
    path('quotationdetail/<slug:slug>/', QuoListDetailView, name='quotationlist_detail'),
    path('quofeedback/<slug:slug>/', SaveQuoFeedback, name='quotation_feedback'),
    path('quofeedback_detail/<slug:slug>/', quofeedback_detail, name='quofeedback_detail'),
    path('addnewquotation/<slug:category>', addNewQuotation, name='addnewquotation'),
]
