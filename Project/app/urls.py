from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('course/<int:course_id>/', views.detail, name='detail'),
    path('course/<int:course_id>/rate/', views.rate, name='rate'),
]

