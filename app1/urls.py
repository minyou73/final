
from django.urls import path
from . import views
from .views import add_score


app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_score/', add_score, name='add_score'),

]