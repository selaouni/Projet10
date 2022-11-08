"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls
from api.views import ProjectViewset, CommentViewset, IssueViewset
from authentication.views import RegisterView, UserByProjectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from rest_framework_nested import routers


router = routers.SimpleRouter()

router.register('project', ProjectViewset, basename='project')
router.register('comment', CommentViewset, basename='comment')
router.register('issue', IssueViewset, basename='issue')

user_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
user_router.register(r'users', ProjectViewset, basename='project-users')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/signup/', RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(user_router.urls)),








    # http://127.0.0.1:8000/accounts/profile/


]
