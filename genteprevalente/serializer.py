from rest_framework import serializers
from genteprevalente.models import Company



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'