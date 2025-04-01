from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profile


urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('', views.injury_list, name='injury_list'),
    path('add/', views.add_injury, name='add_injury'),
    path('login/', auth_views.LoginView.as_view(template_name='InjurySupport/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='InjurySupport/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='InjurySupport/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='InjurySupport/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='InjurySupport/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', profile, name='profile'),
    path('log-symptom/', views.log_symptom, name='log_symptom'),
    path('suggestion/', views.suggestion, name='suggestion'),
    path('rest_and_recovery/', views.rest_and_recovery, name='rest_and_recovery'),
    path('rest_suggestions', views.rest_suggestions, name='rest_suggestions'),
    
]
