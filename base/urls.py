from django.urls import path

from . import views

from .views import*


urlpatterns = [
    path('', views.index, name='index'),
    path('page2', views.index2, name='index2'),
    path('success/', ContactSuccessView.as_view(), name="success"),
]