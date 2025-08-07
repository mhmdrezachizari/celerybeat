from django.urls import path

from .views import GetData

urlpatterns = [
    path('get/' , GetData.as_view() , name='get'),
]