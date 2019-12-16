from django.urls import include, path

from rest_framework.urlpatterns import format_suffix_patterns

from main_app import api, views


view_urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
]

api_root = 'api/1.0/'
api_urlpatterns = [
    # POST
    path(f'{api_root}create_dish/', api.create_dish, name='create-dish'),
]

urlpatterns = view_urlpatterns + format_suffix_patterns(api_urlpatterns)
