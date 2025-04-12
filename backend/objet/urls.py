from django.urls import path, include

from objet import views

urlpatterns = [
    path('latest-objets/', views.LatestObjectsList.as_view()),
    path('search/',views.search),
    path('update-objet/',views.update_objet),
    path('<slug:category_slug>/<slug:object_slug>', views.ObjectDetail.as_view()),
]