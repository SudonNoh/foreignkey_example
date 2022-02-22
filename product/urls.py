from django.urls import URLPattern
from product import views
from django.urls import path

app_name = 'product'

urlpatterns = {
    path('list/', views.Car_information.as_view(), name='car_info')
}