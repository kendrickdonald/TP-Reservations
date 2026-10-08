from rest_framework import serializers
from .models import Salle, Reservation

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = [
            "id",
            "nom",
            "capacite",
            "batiment",
        ]
class ReservationSerializer(serializers.ModelSerializer):
    utilisateur= serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Reservation
        fields = [
            "id",
            "salle",
            "utilisateur",
            "debut",
            "fin",
            "motif",
            "statut",
            "cree_le"

        ]
    def validate(self, data):
        debut = data.get('debut', self.instance.debut if self.instance else None)
        fin = data.get('fin', self.instance.debut if self.instance else None)
        salle = data.get('salle', self.instance.debut if self.instance else None)
        statut = data.get('statut', self.instance.statut if self.instance else "CONFIRMEE")
        if debut and fin and fin<=debut:
            raise serializers.ValidationError({"fin": "une fin ne peut pas etre avant le debut"})
        if statut == "ANNULEE":
            return data
        reservations = Reservation.objects.filter(salle=salle, statut="CONFIRMEE", debutr=fin, finr=debut)
        if self.instance:
            reservations = reservations.exclude(pk=self.instance.pk)
        if reservations.exists():
            raise serializers.ValidationError({"non_field_errors":["une reservation existe deja"]})
        return data
