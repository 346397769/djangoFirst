from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers

# Create your views here.
from django.urls import reverse

from hr.models import Staff, Occupation, ManageDuty, ProDuty, Department, Sex


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
        staff_id = request.GET.get('id')
        staff = Staff.objects.get(pk=staff_id)
        occupations = Occupation.objects.all()
        manage_duties = ManageDuty.objects.all()
        pro_duties = ProDuty.objects.all()
        departments = Department.objects.all()
        return render(request, "staff/update.html",
                      {"staff": staff, "occupations": occupations, "manageDuties": manage_duties,
                       "pro_duties": pro_duties, "departments": departments})
    if request.method == 'POST':
        name = request.POST.get('name')
        id_num = request.POST.get('id_num')
        sex = Sex.objects.filter(num=request.POST.get('sex')).first()
        occupation = Occupation.objects.filter(num=request.POST.get('occupation')).first()
        credentials_no = request.POST.get('credentials_no')
        phone = request.POST.get('phone')
        pro_no = request.POST.get('pro_no')
        manage_duty = ManageDuty.objects.filter(num=request.POST.get('manage_duty')).first()
        pro_duty = ProDuty.objects.filter(num=request.POST.get('pro_duty')).first()
        birthday = request.POST.get('birthday')
        department = Department.objects.filter(num=request.POST.get('department')).first()
        work_time_first = request.POST.get('work_time_first')
        staff_id = request.POST.get('id')
        Staff.objects.filter(id=staff_id).update(name=name, id_num=id_num, sex=sex, occupation=occupation,
                                                 credentials_no=credentials_no, phone=phone, pro_no=pro_no,
                                                 birthday=birthday, manage_duty=manage_duty, pro_duty=pro_duty,
                                                 department=department, work_time_first=work_time_first)
        # Staff.objects.filter(id=staff_id).update(sex=sex)
        return redirect(reverse("hr:show"))


def detail(request):
    if request.method == 'GET':
        staff_id = request.GET.get('id')
        staff = Staff.objects.get(pk=staff_id)
        occupations = Occupation.objects.all()
        manage_duties = ManageDuty.objects.all()
        pro_duties = ProDuty.objects.all()
        departments = Department.objects.all()
        return render(request, "staff/detail.html",
                      {"staff": staff, "occupations": occupations, "manageDuties": manage_duties,
                       "pro_duties": pro_duties, "departments": departments})


def add(request):
    if request.method == 'GET':
        occupations = Occupation.objects.all()
        manage_duties = ManageDuty.objects.all()
        pro_duties = ProDuty.objects.all()
        departments = Department.objects.all()
        return render(request, "staff/add.html",
                      {"occupations": occupations, "manageDuties": manage_duties,
                       "pro_duties": pro_duties, "departments": departments})

    if request.method == 'POST':
        name = request.POST.get('name')
        id_num = request.POST.get('id_num')
        sex = Sex.objects.filter(num=request.POST.get('sex')).first()
        occupation = Occupation.objects.filter(num=request.POST.get('occupation')).first()
        credentials_no = request.POST.get('credentials_no')
        phone = request.POST.get('phone')
        pro_no = request.POST.get('pro_no')
        manage_duty = ManageDuty.objects.filter(num=request.POST.get('manage_duty')).first()
        pro_duty = ProDuty.objects.filter(num=request.POST.get('pro_duty')).first()
        birthday = request.POST.get('birthday')
        department = Department.objects.filter(num=request.POST.get('department')).first()
        work_time_first = request.POST.get('work_time_first')
        Staff.objects.create(name=name, id_num=id_num, sex=sex, occupation=occupation,
                             credentials_no=credentials_no, phone=phone, pro_no=pro_no,
                             birthday=birthday, manage_duty=manage_duty, pro_duty=pro_duty,
                             department=department, work_time_first=work_time_first)
        return redirect(reverse("hr:show"))
