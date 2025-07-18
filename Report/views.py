from django.shortcuts import render,redirect
from Report.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .seed import generate_rank

# Create your views here.

def home(request):
    context={
        'title':"home"
        }
    return render(request,"home.html",context) 

def get_student(request):
    queryset=Student.objects.all()
    
    if request.GET.get("Search"):
        search=request.GET.get("Search")
        queryset=queryset.filter(
            Q(student_name__icontains=search) |
            Q(student_email__icontains=search) |
            Q(student_age__icontains=search) |
            Q(student_id__student_id__icontains=search) |
            Q(department__department__icontains=search)
            
            
            )
    
    paginator = Paginator(queryset, 20)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    queryset = paginator.get_page(page_number)
    return render(request,"students.html",{'queryset':queryset})

def see_marks(request, student_id):
    
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    totalmarks = queryset.aggregate(totalmarks=Sum('marks'))
    total_possible_marks = 100 * queryset.count() 
    percentage = (totalmarks['totalmarks'] / total_possible_marks) * 100 if total_possible_marks > 0 else 0
    student = Student.objects.get(student_id__student_id=student_id)
    
    return render(request, "see_marks.html", {  
        'queryset': queryset,
        'totalmarks': totalmarks,
        'percentage': percentage,
        'student': student,
        
    })
