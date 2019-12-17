from django.urls import include, path

from main_app import api, views


view_urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
]

api_root = 'api/1.0/'
api_urlpatterns = [
    # GET
    path(f'{api_root}get_dishes/', api.get_dishes, name='get-dishes'),
    # POST
    path(f'{api_root}create_dish/', api.create_dish, name='create-dish'),
]

urlpatterns = view_urlpatterns + api_urlpatterns
