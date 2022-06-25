import datetime
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from datetime import date, timedelta
from django.http import HttpResponse



# Create your views here.


def dashboard(request):
    return render(request,'dashboard.html')



def add_client(request):
    if request.method == "POST":
        form = clientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_client')
            except:
                pass
    else:
        form = clientForm()
    return render(request,'add_client.html',{'form':form})

def list_client(request):
    client_list = client.objects.all()
    return render(request,"list_client.html",{'client_list':client_list})

def edit_client(request,pk):
    client_data = client.objects.get(id = pk)
    form = clientForm(instance=client_data)
    if request.method == 'POST':
        form = clientForm(request.POST,instance = client_data)
        if form.is_valid():
            form.save()
            return redirect('list_client')
    
    context = {
        'client_data' :client_data,
        'form':form
    }
    return render(request,'edit_client.html',context)

def delete_client(request,pk):
    clients = client.objects.get(id=pk)
    if request.method =="POST":
        clients.delete()
        return redirect('list_client')
    context = {
        'clients':clients,

    }
    return render(request,'delete_client.html',context)



def add_vps(request):
    if request.method == "POST":
        form = virtual_private_serverForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_vps')
            except:
                pass
    else:
        form  = virtual_private_serverForm()
    return render (request,'add_vps.html',{'form':form})

def list_vps(request):
    vps_list = virtual_private_server.objects.all()
    return render(request,"list_vps.html",{'vps_list':vps_list})


def edit_vps(request,pk):
    vps_data = virtual_private_server.objects.get(id = pk)
    form = virtual_private_serverForm(instance=vps_data)
    if request.method == 'POST':
        form = virtual_private_serverForm(request.POST,instance = vps_data)
        if form.is_valid():
            form.save()
            return redirect('list_vps')
    
    context = {
        'vps_data' :vps_data,
        'form':form
    }
    return render(request,'edit_vps.html',context)


def delete_vps(request,pk):
    vpss = virtual_private_server.objects.get(id = pk)
    if request.method == 'POST':
        vpss.delete()
        return redirect('list_vps')

    context = {
        'vpsss':vpss
    }
    return render(request,'delete_vps.html',context)


def add_trading_account(request):
    if request.method =="POST":
        form = account_masterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_trading_account')
            except:
                pass
    else:
        form = account_masterForm()
    return render(request,'add_trading_account.html',{'form':form})

def list_trading_account(request):
    trading_account_list = account_master.objects.all()
    return render (request,"list_trading_account.html",{'trading_account_list':trading_account_list})


def edit_trading_account(request,pk):
    trading_account_data = account_master.objects.get(id = pk)
    form = account_masterForm(instance=trading_account_data)
    if request.method == 'POST':
        form = account_masterForm(request.POST, instance=trading_account_data)
        if form.is_valid():
            form.save()
            return redirect('list_trading_account')
    
    context = {
        'trading_account_data' :trading_account_data,
        'form':form
    }
    return render(request,'edit_trading_account.html',context)


def delete_trading_account(request,pk):
    tradings = account_master.objects.get(id = pk)
    if request.method =='POST':
        tradings.delete()
        return redirect('list_trading_account')

    context = {}
    return render(request,'delete_trading_account.html',context)

def add_profit(request):
    if request.method =="POST":
        form  = profit_detailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect ('list_profit')
            except:
                pass
    else:
        form = profit_detailsForm()
    return render(request,'add_profit.html',{'form':form})

def list_profit(request):
    profit_list = profit_details.objects.all()
    return render(request,"list_profit.html",{'profit_list':profit_list})

def edit_profit(request,pk):
    profit_data = profit_details.objects.get(id = pk)
    form = profit_detailsForm(instance=profit_data)
    if request.method == 'POST':
        form = profit_detailsForm(request.POST, instance=profit_data)
        if form.is_valid():
            form.save()
            return redirect('list_profit')
    
    context = {
        'profit_data' :profit_data,
        'form':form
    }
    return render(request,'edit_profit.html',context)



def delete_profit(request,pk):
    profits = profit_details.objects.get(id = pk)
    if request.method =='POST':
        profits.delete()
        return redirect('list_profit')

    context = {
        'profits':profits,
    }
    return render(request,'delete_client.html',context)


def add_claim(request):
    if request.method =="POST":
        form = profit_claimForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_claim')
            except:
                pass
    else:
        form = profit_claimForm()
    return render(request,'add_claim.html',{'form':form})


def list_claim(request):
    claim_list = profit_claim.objects.all()
    return render(request,'list_claim.html',{'claim_list':claim_list})


def edit_claim(request,pk):
    claim_data = profit_claim.objects.get(id = pk)
    form = profit_claimForm(instance=claim_data)
    if request.method == 'POST':
        form = profit_claimForm(request.POST, instance=claim_data)
        if form.is_valid():
            form.save()
            return redirect('list_trading_account')
    
    context = {
        'claim_data' :claim_data,
        'form':form
    }
    return render(request,'edit_trading_account.html',context)


def delete_claim(request,pk):
    claims = profit_claim.objects.get(id=pk)

    if request.method =='POST':
        claims.delete()
        return redirect('list_claim')

    context = {
        'claims':claims,
    }
    return render(request,'delete_client.html',context)


def test(request):
    current_date = datetime.date.today().isoformat
    dates = {current_date}
    i = 1
    while i < 10 :
        add_date = (date.today() - timedelta(days = i)).isoformat
        dates.add(add_date)
        i += 1

    context = {
        'dates' :dates
    }
    return render(request,'test.html',context)
   
    
    