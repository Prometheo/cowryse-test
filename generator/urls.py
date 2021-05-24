from django.urls import path

from .views import UuidPairView

urlpatterns = [
    path('pairs/', UuidPairView.as_view()),
]