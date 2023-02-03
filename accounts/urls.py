from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
#   path('signup_psi/', views.signup_psi, name='signup_psi'),
    path('profile/', views.profile, name='profile')
]