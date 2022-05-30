from django.urls import path
from .views import boardsAPI

urlpatterns = [
    path('', boardsAPI.as_view())
]