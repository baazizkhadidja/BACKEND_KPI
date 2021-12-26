from rest_framework import serializers
from .models import Investissement

class InvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investissement
        fields = '__all__'