from rest_framework.serializers import ModelSerializer
from .models import Project, Issue
from.models import Comment, Contributor


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'title',
                  'description', 'type',
                  'author_user_id']


class CommentSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'issue_id': 'issue_id',
    }

    class Meta:
        model = Comment
        fields = ['comment_id', 'description',
                  'author_user_id', 'issue_id',
                  'created_time']


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['issue_id', 'title',
                  'desc', 'tag', 'priority',
                  'status', 'author_user_id',
                  'assignee_user_id',
                  'created_time', 'project_id']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user_id', 'project_id', 'role']
