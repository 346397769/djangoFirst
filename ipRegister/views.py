from django.shortcuts import render
from django.http import HttpResponse, FileResponse
# Create your views here.
from ipRegister.models import IpRegister




def input(request):
    return render(request, "ipRegister/input.html")


def dealSubmit(request):
    reqData = IpRegister()
    # print(request.POST["name"])
    # print(request.POST["ip"])
    # print(request.POST["mac"])
    # print(request.POST["office"])
    # print(request.POST["phone"])
    reqData.name = request.POST["name"]
    reqData.ip = request.POST["ip"]
    reqData.mac = request.POST["mac"]
    reqData.office = request.POST["office"]
    reqData.phone = request.POST["phone"]
    reqData.save()
    return render(request, "ipRegister/afterSubmit.html")


def download(request):
    file = open('static/files/test.docx', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="test.docx"'
    return response