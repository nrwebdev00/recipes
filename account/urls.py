from django.contrib.auth import views as auth_views
from django.urls import path, include
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

    # reset Passwords Urls
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    # Register User URL
    path('register/', views.register, name='account_register'),

    # Dashboard and Index view for Accounts
    path('', views.dashboard, name='account_dashboard'),
]