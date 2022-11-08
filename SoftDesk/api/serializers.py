# from ..authentication.models import User
from rest_framework.serializers import ModelSerializer
from .models import Project, Issue
from.models import Comment, Contributor



# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_id', 'first_name', 'last_name', 'email', 'password']


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'title', 'description', 'type', 'author_user_id']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment_id', 'description', 'author_user_id', 'issue_id', 'created_time']



class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['title', 'desc', 'author_user_id', 'priority', 'tag']


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['author_user_id', 'project_id', 'role']