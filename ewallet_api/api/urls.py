from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('user-list/', views.ShowAll, name='user-list'),
    path('history-list/', views.ShowAllHistory, name='history-list'),
    path('user-create/', views.CreateProduct, name='user-create'),
    path('user-topup/<int:pk>', views.topUpUser, name='user-topup'),
    path('user-transfer/<int:pk>', views.transferUser, name='user-transfer')
]
