from faker import Faker
fake = Faker()
import random
from Report.models import *
from django.db.models import Sum
from datetime import date

def seed_vege(n=10):
    for _ in range (n):
        Department_obj=Department.objects.all()
        random_idx=random.randint(0,len(Department_obj)-1)
        department=Department_obj[random_idx]
        student_id=f"STU-{random.randint(101,999)}"
        student_name=fake.name()
        student_email=fake.email()
        student_age=random.randint(18,25)
        student_address=fake.address()
        
        student_id_object = StudentID.objects.create(student_id=student_id)

        
        student_obj=Student(
            department=department,
            student_id=student_id_object,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address
            )
        student_obj.save()

        
    return 
        
def create_subject_marks():
    name_obj=Student.objects.all()
    sub_obj=Subject.objects.all()
    for student in name_obj:
        for sub in sub_obj:
            SubjectMarks.objects.create ( 
                student=student,
                subject=sub,
                marks=random.randint(0,100)
            )
            
def generate_rank():
    i=1
    #studentmarks is related name of student in SubjectMarks model
    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')  
    for rank in ranks:
        StudentRank.objects.update_or_create(
            student=rank,
            date_of_report_card_generation=date.today(),
            defaults={
                'student_rank': i
            }
        )
        i=i+1
        
            
            

        