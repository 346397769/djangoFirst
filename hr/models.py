from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models


# 员工类
class Staff(models.Model):
    name = models.CharField(max_length=12, null=False)
    # 身份证号
    id_num = models.CharField(max_length=20, null=False)
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT)
    # 职业范围 医生 护士 之类的 外键 职业：医生、护士
    occupation = models.ForeignKey('Occupation', on_delete=models.PROTECT)
    # 资格证书编号
    credentials_no = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=20, null=False)
    # 职业证书编号
    pro_no = models.CharField(max_length=30, null=False)
    # 管理职务 管理职务：书记、院长、主任、护士长、副院长
    manage_duty = models.ForeignKey('ManageDuty', on_delete=models.PROTECT)
    # 专业职务 专业职务：主治医师、主任护士、主任医师、副主任医师
    pro_duty = models.ForeignKey('ProDuty', on_delete=models.PROTECT)
    # 聘任职务
    # appointed_duty = models.ForeignKey('AppointedDuty', on_delete=models.PROTECT)
    # 出生日期
    birthday = models.DateTimeField(null=False)
    # 参加工作时间
    work_time_first = models.DateTimeField(null=False, default=datetime.now)
    # 人员是否激活 用来标志前台是否展示 不展示表示离职 0激活 1不激活
    is_active = models.BooleanField(default=False)
    # 添加时间
    add_time = models.DateTimeField(default=datetime.now)
    # 部门
    department = models.ForeignKey('Department', on_delete=models.PROTECT)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'stuff'


# 职业范围类 医生 护士
class Occupation(models.Model):
    # 编码
    num = models.IntegerField(null=False)
    # 医生 护士 之类的 建议外键 职业：医生、护士
    ocu_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.pro_name

    class Meta:
        db_table = 'occupation'


# 管理职务类 书记、院长、主任、护士长、副院长
class ManageDuty(models.Model):
    # 编码
    num = models.IntegerField(null=False)
    # 管理职务：书记、院长、主任、护士长、副院长
    manage_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.manage_name

    class Meta:
        db_table = 'manage_duty'


# 专业职务类 主治医师、主任护士、主任医师、副主任医师
class ProDuty(models.Model):
    # 编码
    num = models.IntegerField(null=False)
    # 专业职务：主治医师、主任护士、主任医师、副主任医师
    pro_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.pro_name

    class Meta:
        db_table = 'pro_duty'


# 聘任职务类
class AppointedDuty(models.Model):
    # 编码
    num = models.IntegerField(null=False)
    # 聘任职务：
    appointed_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.appointed_name

    class Meta:
        db_table = 'appointed_duty'


# 部门类
class Department(models.Model):
    # 编码
    num = models.IntegerField(null=False)
    # 聘任职务：
    department_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'department'


# 性别类
class Sex(models.Model):
    # 编码
    num = models.IntegerField(null=False)
    # 性别名称
    sex_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.sex_name

    class Meta:
        db_table = 'sex'
