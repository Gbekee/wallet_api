from django.urls import path
from . import views

urlpatterns=[
    path('api/users', views.UserViewSet.as_view(), name='users'),
    path('api/users/<int:pk>', views.UserDetailViewSet.as_view(), name='users')
]