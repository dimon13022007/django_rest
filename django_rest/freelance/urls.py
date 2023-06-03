from . import views
from .views import WomenApiView
from django.urls import path




urlpatterns = [
    path('', views.chat2),
    path('api/v1/womenlist/', WomenApiView.as_view())



]
