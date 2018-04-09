from django.urls import path

from . import views

app_name = 'finances'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('create_entry/', views.CreateEntry.as_view(success_url='/finances'), name='create_entry'),
    path('<int:pk>/', views.UpdateEntry.as_view(success_url='/finances'), name='update_entry'),
    path('delete/<int:pk>/', views.DeleteEntry.as_view(), name='delete_entry'),
]