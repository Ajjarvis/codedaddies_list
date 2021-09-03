from django.urls.conf import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('home/', views.home, name='home'),
]