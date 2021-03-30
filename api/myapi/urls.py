from django.contrib import admin
from django.urls import path
from .views import LawsListView, DailyIdView, UpdateDailyId

app_name = 'myapi'

urlpatterns = [
    path('laws-list', LawsListView.as_view(), name="laws-list"),
    path('daily-id', DailyIdView.as_view(), name="daily-id"),
    path('jobs/update-daily-id/<str:secretkey>', UpdateDailyId.as_view(), name='update-daily-id')
]
