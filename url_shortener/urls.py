from django.urls import path
from .views import UrlsView, UrlDetailView
app_name = "urls"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('urls/', UrlsView.as_view()),
    path('urls/<int:pk>', UrlDetailView.as_view())
]