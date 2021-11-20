from rest_framework import serializers
from api.models import Member

class MemberSerializer(serializers.ModelSerializer):
    mrn = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)
    class Meta:
        model = Member
        # fields = ('name', 'mrn')
        fields = '__all__'
