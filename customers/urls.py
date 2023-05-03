from django.urls import path
from django.contrib.auth import views as view_auth

from customers import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('products/', views.product, name='products'),

    # CRUD order
    path('create_order/<int:pk>/', views.createOrder, name='create_order'),
    path('update_order/<int:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>/', views.deleteOrder, name='delete_order'),

    # Authentication/Authorization
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # User page for users.groups.first().name == 'customer'
    path('user_page/', views.user_page, name='user_page'),
    path('profile/', views.settingsUser, name='profile'),

    # Password reset
    path('password_reset/',
         view_auth.PasswordResetView.as_view(template_name='customers/authentication/password_reset.html')
         , name='password_reset'),
    path('password_reset_done/',
         view_auth.PasswordResetDoneView.as_view(template_name='customers/authentication/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         view_auth.PasswordResetConfirmView.as_view(template_name='customers/authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_complete/',
         view_auth.PasswordResetCompleteView.as_view(template_name='customers/authentication/password_reset_complete.html'),
         name='password_reset_complete'),



]
