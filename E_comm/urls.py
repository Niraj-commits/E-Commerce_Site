from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index,name='index'),
    path('contact/',contact,name='contact'),
    path('create',NewItemCreate,name='create_item'),
    path('<pk>/',item_detail,name = 'item_details'),
]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
