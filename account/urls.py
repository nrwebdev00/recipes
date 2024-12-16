from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='account_login'),

    # Login / Logout Views
    path('login/', auth_views.LoginView.as_view(), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),

    # Change Password Urls
    path(
         'password-change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'
    ),
    path(
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    # Dashboard and Index view for Accounts
    path('', views.dashboard, name='account_dashboard'),
]