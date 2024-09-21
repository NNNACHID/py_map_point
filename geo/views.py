from rest_framework import viewsets
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from .models import PointOfInterest
from .serializers import PointOfInterestSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerializer

    @action(detail=False, methods=["get"])
    def nearby(self, request):
        lat = float(request.query_params.get("lat"))
        lon = float(request.query_params.get("lon"))
        radius = float(request.query_params.get("radius"))
        user_location = GEOSGeometry(f"POINT({lon} {lat})", srid=4326)

        nearby_pois = PointOfInterest.objects.annotate(
            distance=Distance("location", user_location)
        ).filter(distance__lte=radius)

        serializer = self.get_serializer(nearby_pois, many=True)
        return Response(serializer.data)
