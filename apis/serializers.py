from rest_framework import serializers
from apis.models import Vendor, VendorContact, VendorContractDetail


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContact
        fields = '__all__'


class VendorContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContractDetail
        fields = '__all__'
