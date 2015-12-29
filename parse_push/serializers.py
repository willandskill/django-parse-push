from rest_framework import serializers

from .enums import DeviceKind
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    token = serializers.CharField(min_length=20, max_length=100)
    kind = serializers.ChoiceField(DeviceKind.choicify())

    class Meta:
        model = Device
        fields = ('token', 'kind')
