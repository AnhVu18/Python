

from attr import field
from rest_framework.serializers import ModelSerializer
from .models import User, Part, Categorys, Comment, CostOfWork, Document, ExtraWork, Process, Project, SampleDoc, Role, SampleStep, Stage, Work 



class PartSerializer(ModelSerializer):
    class Meta:
        model = Part
        fields = ["id", "tenbophan", "tenphongban", "ngaytao"]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =["id","first_name", "last_name","email", "diachi", "ngaysinh", "sodienthoai", "quyenquanlyduan", "part"]

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields =["id","maduan", "ten", "loaiduan", "duanquantrong", "trangthai", "ngaytao", "ngaybatdau", "ngayketthuc","idbophanthamgiaduan", "idnhanvienthamgia", ]

class StageSerializer(ModelSerializer):
    class Meta:
        model = Stage
        fields =["ten", "ngaytao", "project"]

class CategorysSerializer(ModelSerializer):
    class Meta:
        model = Categorys
        fields = ["ten","mota", "trangthai", "chiphi", "ngaytao", "ngaybatdau", "ngayketthuc", "stage", "role"]

class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = ["ten", "mota", "trangthai", "chiphi", "category", "process", "ngaybatdau", "ngayketthuc", "ngaytao"]