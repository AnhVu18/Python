
from django.urls import path, include, re_path
from . import views
from .admin import admin_site
from rest_framework.routers  import DefaultRouter

router = DefaultRouter()
router.register('Parts', views.PartViewSet)
router.register('User', views.UserViewSet)
router.register('Project', views.ProjectViewSet)
router.register('Stage', views.StageViewSet)
router.register('Categories', views.CategorysViewSet)
router.register('Work', views.WorkViewSet)


urlpatterns = [
   path('', include(router.urls)),
   path('admin/', admin_site.urls) 
]
