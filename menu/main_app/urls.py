from django.urls import include, path

from main_app import api, views


view_urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('order/', views.OrderView.as_view(), name='order'),
]

api_root = 'api/1.0/'
api_urlpatterns = [
    path(f'{api_root}get_dishes/', api.GetDishes.as_view(), name='get-dishes'),
    path(f'{api_root}create_dish/', api.CreateDish.as_view(), name='create-dish'),
]

urlpatterns = view_urlpatterns + api_urlpatterns
