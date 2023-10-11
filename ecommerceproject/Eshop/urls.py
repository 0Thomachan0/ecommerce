from django.urls import path
from Eshop import views
app_name = 'Eshop'
urlpatterns = [
    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodetails,name='procatdetail')
    ]