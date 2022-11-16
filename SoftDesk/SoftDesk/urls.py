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
from api.views import ProjectViewset, CommentViewset, IssueViewset, ContributorViewset
from authentication.views import RegisterView, UserByProjectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework import routers
from rest_framework_nested import routers


router = routers.SimpleRouter()

router.register('project', ProjectViewset, basename='project')
router.register('comments', CommentViewset, basename='comment')
router.register('issues', IssueViewset, basename='issues')

contributor_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
contributor_router.register(r'users', ContributorViewset, basename='project-users')
## generates:
# api/project/{project_id}/users/
# api/project/{project_id}/users/{users_id}/

issue_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
issue_router.register(r'issues', IssueViewset, basename='project-issues')
## generates:
# api/project/{project_id}/issues/
# api/project/{project_id}/issues/{issues_id}/

comment_router = routers.NestedSimpleRouter(issue_router, r'issues', lookup='issues')
comment_router.register(r'comments', CommentViewset, basename='project-comments')


## generates:
# api/project/{project_id}/issues/{issues_id}/comments/
# api/project/{project_id}/issues/{issues_id}/comments/{comments_id}/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(contributor_router.urls)),
    path('api/', include(issue_router.urls)),
    path('api/', include(comment_router.urls)),










]
