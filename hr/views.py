from queue import Queue

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers

# Create your views here.
from django.urls import reverse

from hr.clearFile import myThread1
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
        staff_id = request.POST.get('id')
        staff = Staff.objects.get(pk=staff_id)
        staff.name = request.POST.get('name')
        staff.id_num = request.POST.get('id_num')
        staff.sex_id = request.POST.get('sex')
        staff.occupation_id = request.POST.get('occupation')
        staff.credentials_no = request.POST.get('credentials_no')
        staff.phone = request.POST.get('phone')
        staff.pro_no = request.POST.get('pro_no')
        staff.manage_duty_id = request.POST.get('manage_duty')
        staff.pro_duty_id = request.POST.get('pro_duty')
        staff.birthday = request.POST.get('birthday')
        staff.department_id = request.POST.get('department')
        staff.work_time_first = request.POST.get('work_time_first')
        staff.staff_id = request.POST.get('id')
        staff.save()
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
        file = request.FILES.get('file')
        name = request.POST.get('name')
        id_num = request.POST.get('id_num')
        sex = request.POST.get('sex')
        occupation = request.POST.get('occupation')
        credentials_no = request.POST.get('credentials_no')
        phone = request.POST.get('phone')
        pro_no = request.POST.get('pro_no')
        manage_duty = request.POST.get('manage_duty')
        pro_duty = request.POST.get('pro_duty')
        birthday = request.POST.get('birthday')
        department = request.POST.get('department')
        work_time_first = request.POST.get('work_time_first')
        Staff.objects.create(name=name, id_num=id_num, sex_id=sex, occupation_id=occupation,
                             credentials_no=credentials_no, phone=phone, pro_no=pro_no,
                             birthday=birthday, manage_duty_id=manage_duty, pro_duty_id=pro_duty,
                             department_id=department, work_time_first=work_time_first, head_img=file)
        return redirect(reverse("hr:show"))


def modify_icon(request):
    staff_id = request.POST.get('id')
    staff = Staff.objects.get(pk=staff_id)
    file = request.FILES.get('file')
    if staff.head_img.name:
        myThread1.wait_delete_staff_icon_queue.put("/media/"+staff.head_img.name)
    staff.head_img = file
    staff.save()
    return JsonResponse({"status": 200, "img_src": staff.head_img.name})
