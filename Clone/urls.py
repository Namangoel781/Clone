"""
URL configuration for Clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from web import views 


urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.login_view, name='login_view'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view,name='logout'),
    path('add_invoice/', views.add_invoice, name='addInvoice'),
    path('addinvoice2/', views.add_invoice2, name='add-invoice2'),
    path('company/', views.company, name='company'),
    path('update_company/<int:id>/', views.update_company, name='update_company'),
    path('delete_company/<int:id>/', views.delete_company, name='delete_company'),
    path('all_list/', views.all_list, name='all_list'),
    path('show_client/<int:id>/', views.show_client, name='show_client'),
    path('update_client/<int:id>/', views.update_client, name='update_client'),
    path('service_list/', views.service_list, name='service_list'),
    path('report_client/', views.report_client, name='report_client'),
]
