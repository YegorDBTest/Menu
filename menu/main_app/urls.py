from django.urls import include, path

from main_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
]
