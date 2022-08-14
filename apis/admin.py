from django.contrib import admin
from apis.models import Vendor, VendorContact, VendorContractDetail
# Register your models here.

admin.site.register(Vendor)
admin.site.register(VendorContact)
admin.site.register(VendorContractDetail)