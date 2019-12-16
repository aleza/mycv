from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Personal
from .models import Resume
from .models import Education
from .models import Courses
from .models import Hobbies


def index(request):
    latest_personal_list    = Personal.objects.order_by('name')
    latest_hobbie_list      = Hobbies.objects.order_by('hobbies')[:3]
    latest_education_list   = Education.objects.order_by('-edu_date')[:3]
    latest_courses_list     = Courses.objects.order_by('-cou_date')[:3]
    context = { 'latest_personal_list'  : latest_personal_list, 
                'latest_hobbie_list'    : latest_hobbie_list, 
                'latest_education_list' : latest_education_list,
                'latest_courses_list'   : latest_courses_list
                }
    return render(request, 'cv/index.html', context)

def detail_r(request):  
    latest_resume_list = Resume.objects.order_by('resume_text')
    resume = {'latest_resume_list': latest_resume_list}
    return render(request, 'cv/detail.html', resume)

def detail_e(request, person_id):
    latest_education_list = Education.objects.order_by('-edu_date')
    context = {'latest_education_list': latest_education_list}
    return render(request, 'cv/education.html', context)  

def detail_d(request, person_id):
    latest_data_list = Personal.objects.order_by('name')
    context = {'latest_data_list': latest_data_list}
    return render(request, 'cv/data.html', context)  

def detail_h(request, person_id):
    latest_hobbie_list = Hobbies.objects.order_by('hobbies')[:]
    context = {'latest_hobbie_list': latest_hobbie_list}
    return render(request, 'cv/hobbie.html', context)  

def detail_c(request, person_id):
    latest_courses_list = Courses.objects.order_by('courses')
    context = {'latest_courses_list': latest_courses_list}
    return render(request, 'cv/course.html', context)  


