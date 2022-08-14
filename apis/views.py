from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from apis.models import Vendor, VendorContact, VendorContractDetail
from apis.serializers import VendorSerializer, VendorContactSerializer, VendorContractSerializer

# Create your views here.


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorContactViewSet(viewsets.ModelViewSet):
    queryset = VendorContact.objects.all()
    serializer_class = VendorContactSerializer
    permission_classes = [permissions.IsAuthenticated]

class VendorContractViewSet(viewsets.ModelViewSet):
    queryset = VendorContractDetail.objects.all()
    serializer_class = VendorContractSerializer
    permission_classes = [permissions.IsAuthenticated]