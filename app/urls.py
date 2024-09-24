from django.contrib import admin
from django.urls import path
from corredores.views import corredores_view, new_corredor


urlpatterns = [
    path('admin/', admin.site.urls),

    path('corredores', corredores_view, name='corredores'),
    path('new_corredor', new_corredor, name='new_corredor'),
]
