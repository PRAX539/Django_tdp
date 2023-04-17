from unittest.mock import DEFAULT
from django.db import models

from django.utils.translation import gettext as broker

# Create your models here.


class client(models.Model):
    first_name = models.CharField(max_length = 25)
    middle_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    mobile_number = models.CharField(max_length=20)
    aadhar_card = models.CharField(max_length=20)
    pan = models.CharField(max_length=14)

    class Meta :
        db_table = 'client'

    def __str__(self):
        return self.first_name + ' '+self.middle_name+' '+self.last_name


class virtual_private_server(models.Model):
    company = models.CharField(max_length=25)
    vps_name = models.CharField(max_length=25)
    vps_plan = models.CharField(max_length=50)
    vps_id = models.CharField(max_length=25)
    vps_username = models.CharField(max_length=25)
    vps_password = models.CharField(max_length=25)
    expiration_date = models.DateField()

    class Meta :
        db_table = 'vps'

    def __str__(self):
        return self.vps_name
# trading account is only account master
class broker(models.Model):
    broker_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'broker'

    def __str__(self):
        return self.broker_name


class account_master(models.Model):
    meta_trader  = [
        ('MT4','MT4'),
        ('MT5','MT5')
    ]
    intial_currency = [
        ('USC','USC'),
        ('USD','USD')
    ]
    account_type = [
        ('Standard Cent','Standard Cent'),
        ('Standard','Standard')
    ]

    client = models.ForeignKey(client,on_delete=models.PROTECT)
    broker = models.ForeignKey(broker,max_length=100,on_delete=models.PROTECT)
    account_number = models.CharField(max_length=25)
    meta_trader = models.CharField(max_length=10,choices=meta_trader)
    account_type  = models.CharField(max_length=50,choices=account_type)
    server_name = models.CharField(max_length=30)
    trading_password = models.CharField(max_length=25)
    investor_password = models.CharField(max_length=25)
    leverage = models.IntegerField()
    vps_name = models.ForeignKey(virtual_private_server,on_delete=models.PROTECT)
    currency_unit = models.CharField(max_length=20,choices=intial_currency)
    equity = models.FloatField()
    backup_equity = models.FloatField()
    minimun_equity = models.FloatField()
    TDP_share   = models.FloatField(verbose_name="TDP Share (%)")
    first_referer_name = models.CharField(max_length=50,blank=True,null=True,verbose_name="First Referer Name")
    first_referer_percent = models.FloatField(blank=True,null=True,verbose_name= "First Referer (%)")
    second_referer_name = models.CharField(max_length=50,blank = True,null = True,verbose_name="Second Referer Name")
    second_referer_percent = models.FloatField(blank=True,null = True,verbose_name="Second Referer (%)")
    third_referer_name = models.CharField(max_length=50,blank=True,null = True,verbose_name="Third Referer Name")
    third_referer_percent= models.FloatField(blank=True,null= True, verbose_name="Third Referer (%)")

    class Meta:
        db_table = 'account_master'

    def  __str__(self):
        return self.account_number + ' -  ' + self.client.first_name + ' '+self.client.middle_name + ' ' +self.client.last_name


class profit_details(models.Model):
    account_number = models.ForeignKey(account_master,on_delete=models.PROTECT)
    entry_date = models.DateField()
    profit = models.FloatField()

    class Meta:
        db_table = 'profit_details'

    def __str__(self):
        return self.account_number+' '+self.entry_date + ' ' + self.profit


class profit_claim(models.Model):
    yes_no = [
        ('Yes','Yes'),
        ('No','No')
    ]

    account_number = models.ForeignKey(account_master,on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    total_profit = models.FloatField(blank =True, null=True)
    exchange_rate = models.FloatField(blank =True, null=True)
    total_profit_in_INR = models.FloatField(blank =True, null=True)
    commission_rate = models.FloatField(blank =True, null=True)
    our_share_in_INR = models.FloatField(blank =True, null=True)
    our_share = models.FloatField(blank =True, null=True)
    claim_details = models.TextField(blank=True, null =True)
    received = models.CharField(max_length=5,choices=yes_no,default='No')
    received_date = models.DateField()

    class Meta :
        db_table = 'profit_claim'

    def __str__(self):
        return f"{self.id} account number {self.account_number}"


class claim_settled(models.Model):
    currency = [
        ('INR', 'INR'),
        ('USD','USD')
    ]
    claim_id = models.ForeignKey(profit_claim,on_delete=models.PROTECT)
    claim_settled_in = models.CharField(max_length=15, choices=currency,default='INR')
    amount = models.FloatField(blank=False, null = False)
    settled_account = models.CharField(max_length=255, default = 'indian')
    received_date = models.DateField()

    class Meta:
        db_table = 'claim_settled'

    def __str__(self):
        return self.claim_id + '' + self.amount + '' +self.received_date

