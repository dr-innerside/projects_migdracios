from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_article, name='new-article'),
]