from django.shortcuts import render

# Create your views here.
from hr.models import Staff


def show(request):
    staffs = Staff.objects.filter(is_active=0).all()
    return render(request, "staff/show.html", {"staffs": staffs})
