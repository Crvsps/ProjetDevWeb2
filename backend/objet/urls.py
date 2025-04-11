from django.urls import path, include

from objet import views

urlpatterns = [
    path('latest-objets/', views.LatestObjectsList.as_view()),
    path('objets/search/',views.search),
    path('objets/update-objet/',views.update_objet),
    path('objets/<slug:category_slug>/<slug:object_slug>', views.ObjectDetail.as_view()),
]