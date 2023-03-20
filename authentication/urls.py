from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('login/', views.login_api, name='login_user'),
    path('user/', views.get_user_data, name='get_user_data'),
    path('register/', views.register_api, name='register_user'),
    path('logout/', knox_views.LogoutView.as_views(), name='logout'),
    path('logout_all/', knox_views.LogoutAllView.as_views(), name='logout_all')
]
