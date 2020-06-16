from rest_framework import serializers
from .models import Detail


class DetailSerializer(serializers.ModelSerializer):
    """
    Serializes the Detail model data and returns as JSON
    """
    class Meta:
        model = Detail
        fields = ('guest_name', 'attending', 'not_attending', 'favourite_song',
                  'favourite_drink', 'dietary_requirements', 'additional_info')
