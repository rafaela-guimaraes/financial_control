from django.urls import path

from . import views

app_name = 'finances'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('entry/', views.EntryFormView.as_view(), name='entry'),

]