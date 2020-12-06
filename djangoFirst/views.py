from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def runoob1(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "runoob.html", {"views_list": views_list})


def index(request):
    return render(request, "index.html")


def detail(request):
    return render(request, "detail.html")


# def test2(request):
#
#     # 打开数据库连接
#     db = pymysql.connect("192.168.10.236", "lichao", "123456", "hospital")
#
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # 使用 execute()  方法执行 SQL 查询
#     cursor.execute("select * from reyuan")
#
#     # 使用 fetchone() 方法获取单条数据.
#     data = cursor.fetchall()
#     for row in (data):
#         name = row[1]
#         sex = row[0]
#         age = row[2]
#         print("姓名=%s, 性别=%s,年龄=%s" % (name, sex, age))
#
#     # 关闭数据库连接
#     db.close()
#     return render(request, "detail.html")
