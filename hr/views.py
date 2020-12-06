from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from hr.models import Staff


def show(request):
    staffs = Staff.objects.filter(is_active=0).all()
    return render(request, "staff/show.html", {"staffs": staffs})


def search(request):
    name = request.POST.get('name')
    if name:
        staffs = Staff.objects.filter(name=name).all()
    else:
        staffs = Staff.objects.all()
    return render(request, "staff/show.html", {"staffs": staffs})
    # ret = serializers.serialize("json", staffs)
    # return JsonResponse({'staffs': ret})


def update(request):
    # staffs = Staff.objects.filter(is_active=0).all()
    if request.method == 'GET':
        id = request.GET.get('id')
        staff = Staff.objects.get(pk=id)
        return render(request, "staff/update.html", {"staff": staff})
    if request.method == 'POST':
        pass
