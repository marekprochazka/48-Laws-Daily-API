from django.contrib import admin
from django.urls import path
from .views import LawsListView

app_name = 'myapi'

urlpatterns = [
    path('laws-list', LawsListView.as_view(), name="laws-list")
]
