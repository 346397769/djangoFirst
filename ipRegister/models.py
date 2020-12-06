from django.db import models

# Create your models here.


class IpRegister(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=18, null=True)
    office = models.CharField(max_length=18, null=True)
    mac = models.CharField(max_length=18, null=True)
    ip = models.CharField(max_length=18, null=True)


class PersonIpMac(models.Model):
    office = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    mac = models.CharField(max_length=255, null=False)
    ip = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)

    name_map = {'office_name': 'office', 'name': 'name', 'mac': 'mac', 'ip': 'ip', 'phone': 'phone'}

    def __str__(self):
        return "办公室："+self.office+",姓名："+self.name+",mac"+self.mac

    class Meta:
        db_table = 'person_ip_mac'
