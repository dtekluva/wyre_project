from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'user')
    company_name    = models.CharField(max_length=256, default = " ",null=True, blank = True)
    phone           = models.CharField(max_length=40, default = 0,null=True, blank = True)
    address         = models.TextField(max_length=400, null=True, blank = True)

    def __str__(self):
        return f"{self.company_name} id-({self.id})"


class Branch(models.Model):
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'branch_customer')
    user     = models.ForeignKey(User, on_delete=models.CASCADE, default = 1, related_name = 'branch_user')
    name      = models.CharField(max_length=256, default = " ",null=True, blank = True)
    phone     = models.CharField(max_length=40, default = 0,null=True, blank = True)
    address   = models.TextField(max_length=400, null=True, blank = True)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name


class Location(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'location_customer')
    branch   = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name = 'location_branch')
    user     = models.ForeignKey(User, on_delete=models.CASCADE, default = 1, related_name = 'location_user')
    device_type = models.CharField(max_length=40, null=True, blank = True)
    name        = models.CharField(max_length=256, default = " ",null=True, blank = True)
    phone       = models.CharField(max_length=40, default = 0,null=True, blank = True)
    address     = models.TextField(max_length=400, null=True, blank = True)

    def __str__(self):
        return self.name


class Device(models.Model):
    customer        = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'device_customer')
    location        = models.ForeignKey(Location, on_delete=models.CASCADE, related_name = 'device_location')
    branch        = models.ForeignKey(Branch, on_delete=models.CASCADE, default = 1, related_name = 'device_branch')
    user        = models.ForeignKey(User, on_delete=models.CASCADE, default = 1, related_name = 'device_user')
    device_id       = models.CharField(max_length=40, null=True, blank = True)
    device_type     = models.CharField(max_length=40, null=True, blank = True)
    phone           = models.CharField(max_length=40, default = 0,null=True, blank = True)
    address         = models.TextField(max_length=400, null=True, blank = True)
    name            = models.CharField(max_length=100, null=True, blank = True)
    previous_day_energy = models.IntegerField(null=True, blank=True, default=None)
    previous_day_energy_post_datetime = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.device_id
    

class Reading(models.Model):
    customer        = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'reading_customer', default = 1)
    device          = models.ForeignKey(Device, on_delete=models.CASCADE, related_name = 'reading_device', default = 1)
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'reading_user', default = 1)
    post_datetime= models.DateTimeField(blank = True)
    post_date    = models.DateField(blank = True)
    post_time    = models.TimeField(blank=True)
    voltage_l1_l12  = models.FloatField(null=True, blank=True, default=None)
    voltage_l2_l23  = models.FloatField(null=True, blank=True, default=None)
    voltage_l3_l31  = models.FloatField(null=True, blank=True, default=None)
    current_l1      = models.FloatField(null=True, blank=True, default=None)
    current_l2      = models.FloatField(null=True, blank=True, default=None)
    current_l3      = models.FloatField(null=True, blank=True, default=None)
    kw_l1   = models.FloatField(null=True, blank=True, default=None)
    kw_l2   = models.FloatField(null=True, blank=True, default=None)
    kw_l3   = models.FloatField(null=True, blank=True, default=None)
    kvar_l1 = models.FloatField(null=True, blank=True, default=None)
    kvar_l2 = models.FloatField(null=True, blank=True, default=None)
    kvar_l3 = models.FloatField(null=True, blank=True, default=None)
    kva_l1  = models.FloatField(null=True, blank=True, default=None)
    kva_l2  = models.FloatField(null=True, blank=True, default=None)
    kva_l3  = models.FloatField(null=True, blank=True, default=None)
    power_factor_l1  = models.FloatField(null=True, blank=True, default=None)
    power_factor_l2  = models.FloatField(null=True, blank=True, default=None)
    power_factor_l3  = models.FloatField(null=True, blank=True, default=None)
    total_kw    = models.FloatField(null=True, blank=True, default=None)
    total_kvar  = models.FloatField(null=True, blank=True, default=None)
    total_kva   = models.FloatField(null=True, blank=True, default=None)
    total_pf    = models.FloatField(null=True, blank=True, default=None)
    avg_frequency   = models.FloatField(null=True, blank=True, default=None)
    neutral_current = models.FloatField(null=True, blank=True, default=None)
    volt_thd_l1_l12 = models.FloatField(null=True, blank=True, default=None)
    volt_thd_l2_l23 = models.FloatField(null=True, blank=True, default=None)
    volt_thd_l3_l31 = models.FloatField(null=True, blank=True, default=None)
    current_thd_l1  = models.FloatField(null=True, blank=True, default=None)
    current_thd_l2  = models.FloatField(null=True, blank=True, default=None)
    current_thd_l3  = models.FloatField(null=True, blank=True, default=None)
    current_tdd_l1  = models.FloatField(null=True, blank=True, default=None)
    current_tdd_l2  = models.FloatField(null=True, blank=True, default=None)
    current_tdd_l3  = models.FloatField(null=True, blank=True, default=None)
    kwh_import      = models.FloatField(null=True, blank=True, default=None)
    kwh_export      = models.FloatField(null=True, blank=True, default=None)
    kvarh_import    = models.FloatField(null=True, blank=True, default=None)
    kvah_total      = models.FloatField(null=True, blank=True, default=None)
    max_amp_demand_l1 = models.FloatField(null=True, blank=True, default=None)
    max_amp_demand_l2 = models.FloatField(null=True, blank=True, default=None)
    max_amp_demand_l3 = models.FloatField(null=True, blank=True, default=None)
    max_sliding_window_kw_demand   = models.FloatField(null=True, blank=True, default=None)
    accum_kw_demand    = models.FloatField(null=True, blank=True, default=None)
    max_sliding_window_kva_demand      = models.FloatField(null=True, blank=True, default=None)
    present_sliding_window_kw_demand    = models.FloatField(null=True, blank=True, default=None)
    present_sliding_window_kva_demand   = models.FloatField(null=True, blank=True, default=None)
    accum_kva_demand   = models.FloatField(null=True, blank=True, default=None)
    pf_import_at_maximum_kva_sliding_window_demand = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.post_date} customer-({self.customer})"