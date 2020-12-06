from django.http import HttpResponse

from ipRegister.models import IpRegister, PersonIpMac


def testdb(request):
    # test1 = IpRegister(name='张三')
    # test1.save()
    # return HttpResponse("<p>数据添加成功！</p>")
    one = PersonIpMac.objects.raw("select * from person_ip_mac where name='张三'", translations=PersonIpMac.name_map)[0]
    print(one)
    return HttpResponse("<p>数据添加成功！</p>")
