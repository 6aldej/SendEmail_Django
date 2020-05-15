from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendmes/', include('sendmes.urls', namespace='sendmes')),
]
