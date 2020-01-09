from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drf import views as drf_views
from todo import views 

router = routers.DefaultRouter()
router.register(r'users', drf_views.user_viewset )
router.register(r'todos', views.TodoView, 'todo')
router.register(r'branch', views.BranchViewSet, 'branch')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', include('account.urls')),
    path('admin/', admin.site.urls),
]