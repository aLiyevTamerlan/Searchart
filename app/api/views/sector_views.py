from rest_framework.views import APIView
from rest_framework.response import Response
from app.api.serializer import SectorAllSerializer, SectorSerializer
from app.models import Sector

class SectorAllApiView(APIView):
    def get(self, request):
        sector = Sector.objects.all()
        serializer = SectorAllSerializer(sector, many=True)

        return Response({'sectors':serializer.data})
    
class SectorApiView(APIView):
    def get(self, request, sector_slug):
        sector = Sector.objects.prefetch_related('sub_sectors__indicators').filter(slug=sector_slug)
        serializer = SectorSerializer(sector, many = True)

        return Response({'sectors':serializer.data}) 
    

