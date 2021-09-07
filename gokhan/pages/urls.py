from django.urls import path
from .views import TestView, IndexView, AboutView
from . import views



urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('tests', TestView.as_view(), name="tests"),
    path('hakkimizda', AboutView.as_view(), name="about"),
    path('tests/<slug:category_slug>', views.category_list, name="tests_by_category"),


    ]