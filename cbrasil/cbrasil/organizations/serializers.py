from django.contrib.auth.models import User, Group

from rest_framework import serializers

from cbrasil.organizations.models import Sectors, Organizations


class SectorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sectors
        fields = '__all__'

class OrganizationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organizations
        fields = '__all__'