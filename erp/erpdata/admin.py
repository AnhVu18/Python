from django.contrib import admin
from django import forms
from .models import User, Part, Categorys, Comment, CostOfWork, Document, ExtraWork, Process, Project, SampleDoc, Role, SampleStep, Stage, Work 
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class WorkForm(forms.ModelForm):
    mota = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Work 
        fields = '__all__'




class PartAdmin(admin.ModelAdmin):
    list_display = ["id", "tenbophan", "tenphongban", "ngaytao"]
    search_fields = ["tenbophan", "tenphongban"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name","email","sodienthoai", "diachi", "ngaysinh", ]
    search_fields = ["first_name", "last_name", "email"]

class CategorysAdmin(admin.ModelAdmin):
    list_display = ["ten","mota", "chiphi", "trangthai", "ngaybatdau", "ngayketthuc", "ngaytao", "stage"]
    search_fields = ["ten", "ngaytao"]

class ProjectAdmin(admin.ModelAdmin):
    list_display =["maduan","ten", "loaiduan", "duanquantrong", "trangthai", "ngaybatdau", "ngayketthuc", "ngaytao"]
    search_fields = ["ten", "loaiduan", "maduan"]

class StageAdmin(admin.ModelAdmin):
    list_display = ["ten", "ngaytao", "project"]
    search_fields = ["ten"]

class WorkAdmin(admin.ModelAdmin):
    froms = WorkForm
    list_display = ["ten", "mota", "trangthai", "chiphi", "ngaytao", "category", "process"]
    search_fields = ["ten", "category", "process"]

class ExtraWorkAmin(admin.ModelAdmin):
    list_display = ["ten"]
    search_fields = ["ten"] 

class DocumentAdmin(admin.ModelAdmin):
    list_display = ["ten","ngaytao", "work"]
    search_fields = ["ten"] 

class ProcessAdmin(admin.ModelAdmin):
    list_display = ["ten", "createby", "mota"]
    search_fields = ["ten"]  

class RoleAdmin(admin.ModelAdmin):
    list_display = ["ten", "mausac"]

class SampleDocAdmin(admin.ModelAdmin):
    list_display = ["ten", "ngaytao"]
    search_fields = ["ten"] 

class CostOfWorkAdmin(admin.ModelAdmin):
    list_display = ["staff", "project", "chiphi", "songaycongtac","ngaybatdau","ngayketthuc", "tiencongtac","tienkm", "sokmdadi", "thanhtien"]

class SampleStepAdmin(admin.ModelAdmin):
    list_display = [""]




class ErpAdminSite(admin.AdminSite):
    site_header = 'Quản Trị ERP'


admin_site = ErpAdminSite('myerp')

admin_site.register(User, UserAdmin)
admin_site.register(Part, PartAdmin)
admin_site.register(Categorys, CategorysAdmin)
admin_site.register(Comment)
admin_site.register(CostOfWork, CostOfWorkAdmin)
admin_site.register(Document, DocumentAdmin)
admin_site.register(ExtraWork, ExtraWorkAmin)
admin_site.register(Process, ProcessAdmin)
admin_site.register(Project, ProjectAdmin)
admin_site.register(SampleDoc, SampleDocAdmin)
admin_site.register(Role, RoleAdmin)
admin_site.register(SampleStep)
admin_site.register(Stage, StageAdmin)
admin_site.register(Work, WorkAdmin)



