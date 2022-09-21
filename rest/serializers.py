from rest_framework import serializers
from .models import Studnet

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studnet
        fields = (
            'name', 'age'
        )