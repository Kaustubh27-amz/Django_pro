from django.contrib import admin
from basic.models import Company,Problems,Student,Solution,Solution_Progress
# Register your models here.
admin.site.register(Company)
admin.site.register(Problems)
admin.site.register(Student)
admin.site.register(Solution)
admin.site.register(Solution_Progress)
