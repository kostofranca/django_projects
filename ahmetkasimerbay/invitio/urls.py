from django.urls import path
from . import views

app_name = "invitio"

urlpatterns = [
    path("", views.invite, name="invite"),
]
