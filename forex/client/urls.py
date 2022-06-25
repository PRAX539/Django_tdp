import imp
from django.urls import path
from . import views


urlpatterns = [
   #path('',views.dashboard,name = 'dashboard'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_client',views.add_client,name = 'add_client'),
    path('edit_client/<int:pk>',views.edit_client,name = 'edit_client'),
    path('delete_client/<int:pk>',views.delete_client,name = 'delete_client'),
    path('list_client',views.list_client,name = 'list_client'),
    path('add_trading_account',views.add_trading_account,name = 'add_trading_account'),
    path('edit_trading_account/<int:pk>',views.edit_trading_account,name = 'edit_trading_account'),
    path('delete_trading_account/<int:pk>',views.delete_trading_account,name = 'delete_trading_account'),
    path('add_profit',views.add_profit,name = 'add_profit'),
    path('edit_profit/<int:pk>',views.edit_profit,name = 'edit_profit'),
    path('delete_profit/<int:pk>',views.delete_profit,name = 'delete_profit'),
    path('list_trading_account',views.list_trading_account,name = 'list_trading_account'),
    path('list_profit',views.list_profit,name = 'list_profit'),
    path('add_claim',views.add_claim,name = 'add_claim'),
    path('edit_claim/<int:pk>',views.edit_claim,name = 'edit_claim'),
    path('delete_claim/<int:pk>',views.delete_claim,name = 'delete_claim'),
    path('list_claim',views.list_claim,name = 'list_claim'),
    path('add_vps',views.add_vps,name = 'add_vps'),
    path('edit_vps/<int:pk>',views.edit_vps,name = 'edit_vps'),
    path('delete_vps/<int:pk>',views.delete_vps,name = 'delete_vps'),
    path('list_vps',views.list_vps,name = 'list_vps'),
    path('test',views.test,name ='test'),    



]