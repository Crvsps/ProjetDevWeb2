from django.urls import path, include

from objet import views

urlpatterns = [
    path('latest-objets/', views.LatestObjectsList.as_view()),
    path('objets/search/',views.search),
    path('objets/update-objet/',views.update_objet),
    path('objets/<slug:category_slug>/<slug:object_slug>/', views.ObjectDetail.as_view()),
    path('objets/add-objet/', views.AddObjet.as_view()),
    path('objets/<slug:category_slug>/<slug:object_slug>/delete/', views.DeleteObjet.as_view()),
    path('objet/<slug:objet_id>/pdf/', views.generate_objet_pdf, name='generate_objet_pdf'),
    path('categories/', views.CategoryList.as_view()),
]