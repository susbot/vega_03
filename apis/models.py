from django.db import models

# Create your models here.

class VendorContractDetail(models.Model):
    vendor_contract_title = models.CharField(max_length=10, help_text="10 digits")
    vendor_contract_start_date = models.DateField(editable=True)
    vendor_contract_end_date = models.DateField(editable=True)
    vendor_support_email = models.EmailField()
    vendor_contract_value = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_contract_renewal_date = models.DateField(editable=True)
    vendor_contract_upload = models.CharField(max_length=1, help_text="placeholder")


    def __str__(self):
        return f"{self.vendor_contract_title}"


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=40)
    vendor_phone = models.CharField(max_length=12)
    vendor_soc2 = models.BooleanField()
    vendor_shipping_address = models.CharField(max_length=40)
    vendor_city = models.CharField(max_length=20)
    vendor_state = models.CharField(max_length=2)
    vendor_zipcode = models.CharField(max_length=7)
    """vendor_contact_title = models.ForeignKey(VendorContact,
                               on_delete=models.RESTRICT,
                               related_name="vendorcontact",
                               blank=True,
                               null=True)
                               """
    vendor_contract_details = models.ForeignKey(VendorContractDetail,
                                              on_delete=models.RESTRICT,
                                              related_name="contractdetails",
                                              blank=True,
                                              null=True)

    def __str__(self):
        return f"{self.vendor_name}"


class VendorContact(models.Model):
    vendor_contact_first_name = models.CharField(max_length=30)
    vendor_contact_last_name = models.CharField(max_length=30)
    vendor_contact_phone = models.CharField(max_length=12)
    vendor_contact_email = models.EmailField()
    vendor_contact_title = models.CharField(max_length=40)
    vendor = models.ForeignKey(Vendor, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.vendor_contact_email}"