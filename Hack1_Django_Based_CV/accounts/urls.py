
from django.urls import path
from accounts.views import  SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import ProfileView, AccountLoginView

app_name = 'accounts'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='greetings'), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(template_name='profile.html'), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
  
]





