from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from app.api.serializer.sector_serializer import SectorAllSerializer
from app.models import Sector

class SectorApiTestCase(APITestCase):
    def test_sector(self):
        sec1 = Sector.objects.create(sector_name="Usaqlar")
        sec2 = Sector.objects.create(sector_name="Usaqlar2")
        url = reverse("all-sectors")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(SectorAllSerializer([sec1, sec2], many=True).data, response.data)