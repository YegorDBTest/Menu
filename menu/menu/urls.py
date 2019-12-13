from django.urls import include, path


urlpatterns = [
    path('', include('main_app.urls')),
]
