from rest_framework import serializers

from .enums import DeviceKind
from .models import Device


class DeviceSerializer(serializers.Serializer):
    token = serializers.CharField(min_length=20, max_length=100)
    kind = serializers.ChoiceField(DeviceKind.choicify())

    def create(self, validated_data):
        # TODO: Wrap this logic in a serializer field.
        choices = DeviceKind.choicify()
        dict_ = {k.upper(): v for v, k in choices}
        data = {
            'profile': validated_data['profile'],
            'token': validated_data['token'],
            'kind': dict_.get(validated_data['kind'])
        }
        return Device.objects.create(**data)

    def validate_kind(self, value):
        """ Check that kind is valid. """
        keys = DeviceKind.get_keys()
        if value not in keys:
            raise serializers.ValidationError("Invalid kind ({}) passed! Must be one of {}.".format(value, ', '.join(keys)))
        return value

