from rest_framework import serializers
from api.models import Patient

class UserSerializer(serializers.ModelSerializer):
    mrn = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)
    class Meta:
        model = Patient
        fields = '__all__'