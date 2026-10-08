"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""

from rest_framework import status, viewsets  # noqa: F401  (a utiliser)
from rest_framework.response import Response
from .models import Reservation, Salle
from .serializers import SalleSerializer, ReservationSerializer
from .permissions import IsOwnerOrReadOnly
class SalleViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    permission_classes = [IsOwnerOrReadOnly]
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsOwnerOrReadOnly]