from django.contrib import admin
from Report.models import *
from django.db.models import Sum
# Register your models here.
admin.site.register(Department),
admin.site.register(StudentID),
admin.site.register(Student),
admin.site.register(Subject),
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ('student','subject','marks')
admin.site.register(SubjectMarks,SubjectMarksAdmin),
class StudentRankAdmin(admin.ModelAdmin):
    list_display = ('student','student_rank','total_marks','date_of_report_card_generation')
    def total_marks(self,obj):
        return obj.student.studentmarks.aggregate(total_marks=Sum('marks'))['total_marks']
    total_marks.short_description = 'Total Marks'
    
admin.site.register(StudentRank,StudentRankAdmin)

