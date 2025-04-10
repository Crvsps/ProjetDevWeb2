from django.urls import path, include

from objet import views

urlpatterns = [
    path('latest-objets/', views.LatestObjectsList.as_view()),
]