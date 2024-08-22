from django.urls import path
from Basic_app import views


#TEMPLATES URLS
app_name = 'Basic_app'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
