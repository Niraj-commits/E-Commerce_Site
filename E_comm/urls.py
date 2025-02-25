from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('favicon.ico/', lambda request: HttpResponse(status=204)),
    path('', index,name='index'),
    path('contact/',contact,name='contact'),
    path('user_detail/',myProducts,name = 'myProducts'),
    path('create/',NewItemCreate,name='create_item'),
    path('category/',NewCategoryCreate,name='create_category'),
    path('<pk>/',item_detail,name = 'item_details'),
    path('<pk>/delete/',deleteItem,name = 'delete_items'),
    path('<pk>/edit/',editProducts,name = 'edit_items'),

]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
