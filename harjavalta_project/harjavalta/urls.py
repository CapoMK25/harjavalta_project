from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('koti/', views.koti, name='koti'),
    path('työpaikat/', views.työpaikat, name='työpaikat'),
    path('yrityksille/', views.yrityksille, name='yrityksille'),
    path('työntekijöille/', views.työntekijöille, name='työntekijöille'),
    path('info/', views.info, name='info'),
]