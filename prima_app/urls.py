from django.urls import path
from .views import homepage,lista_meccanici

app_name="prima_app"

urlpatterns=[
    path('',homepage,name='homepage'),
    path('lista_meccanici',lista_meccanici,name='lista_meccanici')
]