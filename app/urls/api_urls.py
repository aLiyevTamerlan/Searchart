from django.urls import path, include
from app.api.views import SectorAllApiView, SectorApiView
urlpatterns = [
    path('sectors/', SectorAllApiView.as_view(), name="all-sectors"),
    path('sectors/<slug:sector_slug>/', SectorApiView.as_view())
]