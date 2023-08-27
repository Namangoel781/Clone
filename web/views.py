from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from num2words import num2words



# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':

            fm = UserLogin(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                userObj = authenticate(username=uname, password=upass)
                if userObj is not None:
                    login(request, userObj)

                    return HttpResponseRedirect('/home/')
        else:
            fm = UserLogin()
        return render(request,'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/home/')


    
def logout_view(request):
     
     logout(request)

     return HttpResponseRedirect('/')



def home(request):
        return render(request, 'home.html')
        





     



# client model form
def add_invoice(request):
        all_list = Company.objects.all()
        if request.user.is_authenticated:
            if request.method == "POST":
                clientFm = ClientForm(request.POST)

                if clientFm.is_valid():
                    comp = clientFm.cleaned_data['company_name']
                    gst = clientFm.cleaned_data['gst_number']
                    cntry = clientFm.cleaned_data['country']
                    sts = clientFm.cleaned_data['state']
                    add = clientFm.cleaned_data['address']

                    obj = Client(company_name=comp,gst_number=gst,country = cntry,state=sts,address=add)
                    obj.save()

                    messages.success(
                        request , "Your 'client' form has been saved successfully."
                    )

                    clientFm = ClientForm()

                    context = {'clientfm' : clientFm, 'qs':all_list}
            else:
                clientFm = ClientForm()
                context = {'clientfm':clientFm, 'qs':all_list}
            return render(request, 'addinvoice.html', context)

        else:
            return HttpResponseRedirect('/')

# service model form
def add_invoice2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            serviceFm = ServicesForm(request.POST)

            if serviceFm.is_valid():
                cname = serviceFm.cleaned_data['client']
                dict = serviceFm.cleaned_data['description']
                quant = serviceFm.cleaned_data['quantity']
                amt = serviceFm.cleaned_data['amount']

                serObj = Services(client=cname,description=dict,quantity=quant,amount=amt)
                serObj.save()
                
                messages.success(
                    request , "Your 'client' form has been saved successfully."
                )

                serviceFm = ServicesForm()
        else:
            serviceFm = ServicesForm()
        return render(request, 'addinvoice.html', {'serviceFm' : serviceFm})
        
    else:
        return HttpResponseRedirect('/')
    
def company(request):
     if request.user.is_authenticated:
         if request.method == "POST":
             CompanyFm = CompanyForm(request.POST)
             if CompanyFm.is_valid():
                client = request.POST["client"]
                company_name = request.POST["company"]
                handle_by = request.POST["handle"]
                email = request.POST["email"]
                phone = request.POST["phone"]
                account_number = request.POST["acct"]
                ifsc_code = request.POST["ifsc"]
                bank_name = request.POST["bank"]
                gst_number = request.POST["gst"]

                new_provider = Company(client = client, company_name = company_name, handle_by = handle_by, 
                email = email, phone = phone, account_number = account_number, ifsc_code = ifsc_code, 
                bank_name = bank_name, gst_number = gst_number)
                new_provider.save()

                messages.success(
                    request , "Your 'client' form has been saved successfully."
                )

                CompanyFm = CompanyForm()
                provider = Company.objects.all()
                context = {'CompanyFm': CompanyFm, 'provider':provider}
         else:
             CompanyFm = CompanyForm
             provider = Company.objects.all()
             context = {'CompanyFm':CompanyFm, 'provider':provider}
             return render(request, 'addinvoice.html' , context) 
     else:
         return HttpResponseRedirect('/')

def update_company(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Company.objects.get(pk=id)
            fm = CompanyForm(request.POST, isinstance=obj)
            if fm.is_valid():
                fm.save()

                messages.success(
                    request, "Successfully updated, You can go back ! "
                )
        else:
            obj = Company.objects.get(pk=id)
            fm = CompanyForm(instance=obj)

        return render(request, 'update_comp.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')
    
def delete_company(request, id):
     if request.user.is_authenticated:
         if request.method == 'POST':
             obj = Company.objects.get(pk=id)
             obj.delete()
         return HttpResponseRedirect('/company/')
     else:
         return HttpResponseRedirect('/')
    
def all_list(request):
    show_list = Client.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ClientForm(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm = ClientForm()

            context = {'allList': show_list}
        return render(request, 'all_list.html', context)
    else:
        return HttpResponseRedirect('/')
    
def show_client(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Client.objects.get(pk=id)
                  
        else:
            obj = Client.objects.get(pk=id)
            
            context = {'show_list':obj}

        return render(request, 'show.html', context)
    else:
        return HttpResponseRedirect('/')
    
def update_client(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Client.objects.get(pk=id)
            fm = ClientForm(request.POST, instance=obj)
            if fm.is_valid():
                fm.save()

                messages.success(
                    request, "Successfully updated, You can go back !"
                )
        else:
            obj = Client.objects.get(pk=id)
            fm = ClientForm(instance=obj)

        return render(request, 'update_client.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')
    
def delete_company(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Client.objects.get(pk=id)
            obj.delete()
        return HttpResponseRedirect('/all_list/')
    else:
        return HttpResponseRedirect('/')
    
def service_list(request):
    serviceList = Services.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ServicesForm(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm = ServicesForm()

            context = {'serviceList': serviceList}
        return render(request, 'show_service.html', context)
    else:
        return HttpResponseRedirect('/')
    
def report_client(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Client.objects.all()
                  
        else:
            obj = Client.objects.all()
            
            context = {'report_list':obj}

        return render(request, 'report.html', context)
    else:
        return HttpResponseRedirect('/')
    
def review(request, pk):
    if request.user.is_authenticated:
        clientData =  Client.objects.get(id=pk)
        try:
            companyData = Company.objects.get(client_id=pk)
        except Company.DoesnotExit:
            companyData = {'key':'val'}
        try:
            servicesData = Services.objects.filter(client_id=pk)
        except Services.DoesnotExit:
            servicesDataData = {'key':'val'}

        context = {'clientData': clientData, 'companyData': companyData,'servicesData': servicesData}
        return render(request, 'review.html', context)
    
def pdf_report(request, pk):
    if request.user.is_authenticate:
        clientData = Client.objects.get(id=pk)
        try:
            companyData = Company.objects.get(client_id=pk)
        except Company.DoesNotExist:
            companyData = {'Key': 'Val'}
        try:
            servicesData = Services.objects.filter(client_id=pk)
        except Services.DoesNotExist:
            servicesData = {'Key': 'Val'}
        try:
            total_amt = []
            for i in servicesData:
                val = i.amount * i.quantity
                total_amt.append(val)
            
            total_amt2 = sum(total_amt)
            gst = 0.18
            gst_amt = total_amt2 * gst
            price_with_gst = total_amt2 * (total_amt2 * gst)

            word_amt = num2words(price_with_gst, Lang="en_IN")

        except Exception as e:
            pass

        context = {'clientData': clientData, 'companyData':companyData, 'servicesData':servicesData, 'gst_amt':gst_amt, 'price_with_gst':price_with_gst, 'word_amt':word_amt}

        return render(request, 'pdfReport.html', context)
    else:
        return HttpResponseRedirect('/')