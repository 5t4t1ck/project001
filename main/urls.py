from django.urls import URLPattern, path, include
from .views import hompage

app_name = "main"

urlpatterns = [
    path("", hompage, name="hompage"),
]
