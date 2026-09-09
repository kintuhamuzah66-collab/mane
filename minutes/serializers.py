from rest_framework import serializers
from minutes.models import Minutes

class MinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minutes
        fields = "__all__"