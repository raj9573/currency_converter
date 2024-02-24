from django.urls import path
from .import views 

urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('convert/', views.currency_converter, name='currency_converter'),
]
