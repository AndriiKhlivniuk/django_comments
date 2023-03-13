from django.urls import path, include
from . import views

app_name = 'comments'
urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('', views.comments, name='comments'),
    path('add/', views.add_comment, name='add_comment'),
    path('thanks/', views.thanks, name='thanks'),
    path('add1/', views.add_answer, name='add_answer')
]
