from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path(
        'reset_password',
        views.MyPasswordResetView.as_view(template_name='registration/reset_pw.html'),
        name='reset_password'
    ),
    path('create-post', views.create_post, name="create_post")
]
