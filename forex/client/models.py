from unittest.mock import DEFAULT
from django.db import models
from numpy import True_, true_divide

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
class account_master(models.Model):
    account_type  = [
        ('mt4','mt4'),
        ('mt5','mt5')
    ]
    intial_currency = [
        ('cent','cent'),
        ('dollar','dollar')
    ]

    client = models.ForeignKey(client,on_delete=models.PROTECT)
    broker = models.CharField(max_length=25)
    account_number = models.CharField(max_length=25)
    meta_trader = models.CharField(max_length=10,choices=account_type)
    account_type  = models.CharField(max_length=25)
    server_name = models.CharField(max_length=30)
    trading_password = models.CharField(max_length=25)
    investor_password = models.CharField(max_length=25)
    leverage = models.IntegerField()
    vps_name = models.ForeignKey(virtual_private_server,on_delete=models.PROTECT)
    currency_unit = models.CharField(max_length=20,choices=intial_currency)
    equity = models.FloatField()
    backup_equity = models.FloatField()
    minimun_equity = models.FloatField()
    TDP_share = models.FloatField()
    first_referer_name = models.CharField(max_length=50,blank=True,null=True)
    first_referer_percent = models.FloatField(blank=True,null=True)
    second_referer_name = models.CharField(max_length=50,blank = True,null = True)
    second_referer_percent = models.FloatField(blank=True,null = True)
    third_referer_name = models.CharField(max_length=50,blank=True,null = True)
    third_referer_percent= models.FloatField(blank=True,null= True)

    class Meta:
        db_table = 'account_master'

    def  __str__(self):
        return self.account_number 


class profit_details(models.Model):
    account_number = models.ForeignKey(account_master,on_delete=models.PROTECT)
    entry_date = models.DateField(unique=True)
    profit = models.FloatField()

    class Meta:
        db_table = 'profit_details'

    def __str__(self):
        return self.entry_date + ' ' + self.profit


class profit_claim(models.Model):
    
    account_number = models.ForeignKey(account_master,on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    total_profit = models.FloatField(blank =True, null=True)
    exchange_rate = models.FloatField(blank =True, null=True)
    total_profit_in_INR = models.FloatField(blank =True, null=True)
    commission_rate = models.FloatField(blank =True, null=True)
    our_share_in_INR = models.FloatField(blank =True, null=True)
    our_share = models.FloatField(blank =True, null=True)

    class Meta :
        db_table = 'profit_claim'

    def __str__(self):
        return self.account_number + ' ' + self.start_date + ' ' + self.end_date + ' ' +self.total_profit + ' ' + self.our_share 


class claim_settled(models.Model):
    currency = [
        ('INR', 'INR'),
        ('USD','USD')
    ]
    claim_id = models.ForeignKey(profit_claim,on_delete=models.PROTECT)
    claim_settled_in = models.CharField(max_length=15, choices=currency,default='INR')
    amount = models.FloatField(blank=False, null = False)
    settlement_method = models.CharField(max_length=255, default = 'transfered')
    received_date = models.DateField()

    class Meta:
        db_table = 'claim_settled'

    def __str__(self):
        return self.claim_id + '' + self.amount + '' +self.received_date