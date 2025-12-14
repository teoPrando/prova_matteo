from django.urls import path
from .views import homepage,meccanici,autovetture

app_name="prima_app"

urlpatterns=[
    path('',homepage,name='homepage'),
    path('meccanici',meccanici,name='meccanici'),
    path('autovetture',autovetture,name='autovetture')
]