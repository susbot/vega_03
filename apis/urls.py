from django.urls import include, path
from rest_framework import routers
from apis import views


router = routers.DefaultRouter()
router.register('vendor', views.VendorViewSet, basename='vendor')
router.register('vendor_contact', views.VendorContractViewSet, basename='vendor_contact')
router.register('vendor_contract', views.VendorContactViewSet, basename='vendor_contract')


urlpatterns = [
    path('', include(router.urls)),

]