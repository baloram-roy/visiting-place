from django.conf import settings
from django.conf.urls.static import static
from place.views import PlaceListView
from django.urls import path
from .views import (
    PlaceDetailView,
    PlaceListView,
    PlaceCreateView,
    PlaceUpdateView,
    PlaceDeleteView,
)


urlpatterns = [
    path('', PlaceListView.as_view(), name='place-list'),
    path('place/new/', PlaceCreateView.as_view(), name='place-create'),
    path('place/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    path('place/<int:pk>/update/', PlaceUpdateView.as_view(), name='place-update'),
    path('place/<int:pk>/delete/', PlaceDeleteView.as_view(), name='place-delete'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)