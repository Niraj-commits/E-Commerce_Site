from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('favicon.ico/', lambda request: HttpResponse(status=204)),
    path('', home,name='index'),
    path('contact/',contact,name='contact'),
    path('myProducts/',MyProducts,name = 'myProducts'),
    path('create/',NewProduct,name='create_item'),
    path('mycategories/',NewCategory,name='create_category'),
    path('category/',ViewCategory,name='MyCategories'),
    path('category/<pk>',EditCategory,name='edit_category'),
    path('category/<pk>/delete',DeleteCategory,name='delete_category'),
    path('<pk>/',ViewProduct,name = 'item_details'),
    path('<pk>/delete/',DeleteProducts,name = 'delete_items'),
    path('<pk>/edit/',EditProducts,name = 'edit_items'),

]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
