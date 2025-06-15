

from django.urls import path
from .views import IndexView, QuoteCreateView, EditView, QuoteDeleteView, main

urlpatterns = [
    path("", main, name="index"),
    path("<int:page>", main, name="index_paginated"),
    path("create/", QuoteCreateView.as_view(), name="create"),
    path("edit/<str:pk>/", EditView.as_view(), name="edit"),
    path("delete/<str:pk>/", QuoteDeleteView.as_view(), name="delete"),
]
