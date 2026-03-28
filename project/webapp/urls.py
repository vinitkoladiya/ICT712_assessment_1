from django.urls import path
from . import views

urlpatterns = [
    path('session-demo/', views.session_demo, name='session_demo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.protected_view, name='protected'),
    path('contact/', views.contact_view, name='contact'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
]