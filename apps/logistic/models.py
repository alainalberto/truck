from django.db import models

from django.contrib.auth.models import User

from apps.accounting.models import Account, Invoice, Fee, Payment

# Create your models here.


class TrucksLogt(models.Model):
    id_tuk = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=45, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    serial = models.CharField(max_length=20, blank=True, null=True)
    number = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    insp_date_exp = models.DateField(blank=True, null=True)
    regit_date_exp = models.DateField(blank=True, null=True)
    deactivate = models.BooleanField(default=False)
    deactivate_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.number)

class DriversLogt(models.Model):
    id_dr = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, blank=True, null=True)
    comercial_name = models.CharField(max_length=45, blank=True, null=True)
    license_numb = models.CharField(max_length=45)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    lic_date_exp = models.DateField(blank=True, null=True)
    medicard_date_exp = models.DateField(blank=True, null=True)
    drugtest_date = models.DateField(blank=True, null=True)
    drugtest_date_exp = models.DateField(blank=True, null=True)
    mbr_date = models.DateField(blank=True, null=True)
    mbr_date_exp = models.DateField(blank=True, null=True)
    begining_date = models.DateField(blank=True, null=True)
    deactivate = models.BooleanField(default=False)
    date_deactivated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class DispatchLogt(models.Model):
    id_dsp = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    deactivate = models.BooleanField(default=False)
    date_deactivated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Load(models.Model):
    id_lod = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    driver = models.ForeignKey(DriversLogt, blank=True, null=True, on_delete=models.CASCADE)
    dispatch = models.ForeignKey(DispatchLogt, blank=True, null=True, on_delete=models.CASCADE)
    broker = models.CharField(max_length=45, blank=True, null=True)
    pickup_from = models.CharField(max_length=45, blank=True, null=True)
    pickup_date = models.DateField(blank=True, null=True)
    deliver = models.CharField(max_length=45, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    number = models.CharField(max_length=20,blank=True, null=True)
    paid = models.BooleanField(default=True)
    note = models.CharField(max_length=225, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.number)

class PermissionsLogt(models.Model):
    id_prm = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    usdot = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    usdot_pin = models.CharField(max_length=20, blank=True, null=True)
    txdmv = models.CharField(max_length=20, blank=True, null=True)
    txdmv_user = models.CharField(max_length=20, blank=True, null=True)
    txdmv_passd = models.CharField(max_length=45, blank=True, null=True)
    txdmv_date = models.DateField(blank=True, null=True)
    txdmv_date_exp = models.DateField(blank=True, null=True)
    mc = models.CharField(max_length=20, blank=True, null=True)
    mc_pin = models.CharField(max_length=20, blank=True, null=True)
    boc3 = models.BooleanField(default=True)
    boc3_date = models.DateField(blank=True, null=True)
    ucr = models.BooleanField(default=True)
    update = models.DateField(blank=True, null=True)


class InsuranceLogt(models.Model):
    id_inr = models.AutoField(primary_key=True)
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    accounts = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    down_payment = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pilicy_efective_date = models.DateField(blank=True, null=True)
    pilicy_date_exp = models.DateField(blank=True, null=True)
    liability = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pilicy_liability = models.CharField(max_length=45, blank=True, null=True)
    cargo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    cargo_pilicy = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    physical_damage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    physical_damg_pilicy = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sale_type = models.CharField(max_length=20, blank=True, null=True)
    sale_date_fee = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fee_value = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    paid = models.BooleanField(default=True)


class IftaLogt(models.Model):
    id_ift = models.AutoField(primary_key=True)
    trucks = models.ForeignKey(TrucksLogt, on_delete=models.CASCADE)  # Field name made lowercase.
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    driver = models.ForeignKey(DriversLogt, on_delete=models.CASCADE)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    milles = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gallons = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)


class TravelExpense(models.Model):
    id_tre = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(Account, on_delete=models.CASCADE)  # Field name made lowercase.
    users = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    driver = models.ForeignKey(DriversLogt, on_delete=models.CASCADE)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)


class LoadsHasFee(models.Model):
    id_lfe = models.AutoField(primary_key=True)
    loads = models.ForeignKey(Load, on_delete=models.CASCADE)  # Field name made lowercase.
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

class InvoicesHasLoad(models.Model):
    id_inl = models.AutoField(primary_key=True)
    invoices = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Field name made lowercase.
    loads = models.ForeignKey(Load, on_delete=models.CASCADE)  # Field name made lowercase.

class DriversHasPayment(models.Model):
    id_pym = models.AutoField(primary_key=True)
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE)  # Field name made lowercase.
    driver = models.ForeignKey(DriversLogt, on_delete=models.CASCADE)  # Field name made lowercase.

class DispatchHasPayment(models.Model):
    id_pym = models.AutoField(primary_key=True)
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE)  # Field name made lowercase.
    dispatch = models.ForeignKey(DispatchLogt, on_delete=models.CASCADE)  # Field name made lowercase.

