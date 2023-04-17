from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(client)
admin.site.register(virtual_private_server)
admin.site.register(account_master)
admin.site.register(profit_details)

