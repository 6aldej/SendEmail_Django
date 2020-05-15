from django.urls import path
from . import views 


app_name = 'sendmes'
urlpatterns = [
    path('send/', views.send_mes, name='send'),
    path('list/', views.last_tasks, name='emails'),
]
