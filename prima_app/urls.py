from django.urls import path
from .views import homepage

app_name="prima_app"

urlpatterns=[
    path('homepage',homepage,name='homepage')
]