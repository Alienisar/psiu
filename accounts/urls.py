from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_psi/', views.signupsi, name='signup_psi')
]