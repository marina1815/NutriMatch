from django.urls import path
from .views import home, form_page

urlpatterns = [
    path("", home, name="home"),
    path("form/", form_page, name="form"),
]