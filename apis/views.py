from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from apis.models import Vendor, VendorContact, VendorContractDetail
from apis.serializers import (VendorSerializer,
                              VendorContactSerializer,
                              VendorContractSerializer,
                              # AuthTokenSerializer,
                              )

# Create your views here.


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class VendorContactViewSet(viewsets.ModelViewSet):
    queryset = VendorContact.objects.all()
    serializer_class = VendorContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class VendorContractViewSet(viewsets.ModelViewSet):
    queryset = VendorContractDetail.objects.all()
    serializer_class = VendorContractSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class CreateTokenView(ObtainAuthToken):
    # serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES