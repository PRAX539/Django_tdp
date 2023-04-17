import datetime
import json
from django.utils.dateparse import parse_date
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from datetime import date, timedelta
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg, Count, Min, Sum





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
                return redirect ('add_profit')
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
    return render(request,'edit_claim.html',context)


def delete_claim(request,pk):
    claims = profit_claim.objects.get(id=pk)

    if request.method =='POST':
        claims.delete()
        return redirect('list_claim')

    context = {
        'claims':claims,
    }
    return render(request,'delete_client.html',context)


   
    

def add_settlement(request):
    if request.method == "POST":
        form = claim_settledForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_settlement')
            except:
                pass
    else:
        form = claim_settledForm()
    return render(request,'add_settlement.html',{'form':form})




def delete_settlement(request,pk):
    claims = claim_settled.objects.get(id=pk)

    if request.method =='POST':
        claims.delete()
        return redirect('list_settlement')

    context = {
        'claims':claims,
    }
    return render(request,'delete_settlement.html',context)


def edit_settlement(request,pk):
    claim_data = claim_settled.objects.get(id = pk)
    form = claim_settledForm(instance=claim_data)
    if request.method == 'POST':
        form = claim_settledForm(request.POST, instance=claim_data)
        if form.is_valid():
            form.save()
            return redirect('list_settlement')
    
    context = {
        'claim_data' :claim_data,
        'form':form
    }
    return render(request,'edit_settlement.html',context)



def list_settlement(request):
    claim_settlement = claim_settled.objects.all()
    return render(request,'list_settlement.html',{'claim_settlement':claim_settlement})





def add_broker(request):
    if request.method == "POST":
        form = brokerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_broker')
            except:
                pass
    else:
        form = brokerForm()
    return render(request,'add_broker.html',{'form':form})




def edit_broker(request,pk):
    broker_data = broker.objects.get(id = pk)
    form = brokerForm(instance=broker_data)
    if request.method == 'POST':
        form = brokerForm(request.POST, instance=broker_data)
        if form.is_valid():
            form.save()
            return redirect('list_broker')
    
    context = {
        'broker_data' :broker_data,
        'form':form
    }
    return render(request,'edit_settlement.html',context)



def delete_broker(request,pk):
    brokers = broker.objects.get(id=pk)

    if request.method =='POST':
        brokers.delete()
        return redirect('list_broker')

    context = {
        'brokers':brokers,
    }
    return render(request,'delete_broker.html',context)

def list_broker(request):
    broker_list = broker.objects.all()
    return render(request,'list_broker.html',{'broker_list':broker_list})



def table_profit(request):
    account_number_id = request.GET.get('account_number_id')
    data_filtered = profit_details.objects.filter(account_number_id = account_number_id).order_by('-entry_date')[0:10]
    return render(request,'table_profit.html',{'data_filtered':data_filtered})

def test_two(request):
    
    account_number_id = request.GET.get('account_number_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    profit_return =  profit_details.objects.filter(account_number_id = account_number_id).filter(entry_date__range=[start_date,end_date]).aggregate(Sum('profit'))

    final_amount = profit_return['profit__sum']
    context = {
        'final_amount':final_amount
    }
 
    return render(request,'test_two.html',context)

def test_three(request):
    account_number_id  =request.GET.get('account_number_id')
    # account_number_id = 3
    commission = account_master.objects.filter(id = account_number_id).values_list('TDP_share',flat=True).first()
    context = {
        'commission' : commission
   }
    return render(request,'test_three.html',context)


def report_generator(request):

    account_details = account_master.objects.all()

    context = {
        'account_details': account_details
    }


    return render(request,'reports.html',context)

def reports(request):
    account_number = request.GET.get('account_number')
    start_date = request.GET.get('start_date')
    format_start_date = parse_date(start_date)
    end_date = request.GET.get('end_date')
    format_end_date= parse_date(end_date)
   
  
    profits = profit_details.objects.filter(account_number_id = account_number).filter(entry_date__lte = end_date).filter(entry_date__gte = start_date)
    profit_return =  profit_details.objects.filter(account_number_id = account_number).filter(entry_date__range=[start_date,end_date]).aggregate(Sum('profit'))
    final_amount = profit_return['profit__sum']
    account_details = account_master.objects.filter(id = account_number)

    client_id = account_master.objects.filter(id = account_number).values_list('client_id',flat=True).first()
    client_details = client.objects.filter(id = client_id)
    context = {
        'account_details':account_details,
        'format_start_date':format_start_date,
        'format_end_date':format_end_date,
        'client_details':client_details,
        'profits':profits,
        'final_amount':final_amount,
    }
    return render(request,'final_reports.html',context)


def account_name(request):
    account_number_id = request.GET.get('account_number_id')
    client_id = account_master.objects.filter(id = account_number_id).values_list('client_id',flat=True).first()
    client_details = client.objects.filter(id = client_id)

    context = {
        'client_details':client_details
    }

    return render(request,'account_name.html',context)

def currency_unit(request):
    account_number_id = request.GET.get('account_number_id')
    currency_unit = account_master.objects.filter(id = account_number_id).values_list('currency_unit',flat=True).first()
   

    context = {
        'currency_unit':currency_unit
    }

    return render(request,'currency_unit.html',context)


