from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwnerOrReadOnly, IsStaffpermission
from django.db.models import Q

from api.models import Project, Comment, Issue, Contributor
from .serializers import ProjectSerializer, CommentSerializer, IssueSerializer, ContributorSerializer

from django.shortcuts import get_object_or_404
# from rest_framework import permissions

#
# class UserViewset(ModelViewSet):
#
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         queryset = Usr.objects.all()


class ProjectViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsStaffpermission]
    serializer_class = ProjectSerializer

    def get_queryset(self, *args, **kwargs):
        # Nous récupérons tous les produits dans une variable nommée queryset
        user = self.request.user
        # queryset = Project.objects.filter(author_user_id=user or contributor = user)
        # queryset = Project.objects.filter(
        #     Q(author_user_id=user.id) | Q(contributor=user.id)
        # )

        queryset = Project.objects.filter(author_user_id=user.id) | Project.objects.filter(contributor=user.id)
        # Vérifions la présence du paramètre ‘project_id’ dans l’url et si oui alors appliquons notre filtre
        project_id = self.request.GET.get('project_id')
        # qs = Album.objects.prefetch_related('tracks')

        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)

        return queryset

    def put_queryset(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = ProjectSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_queryset(self, format=None):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_queryset(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class IssueViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = IssueSerializer

    def get_queryset(self, *args, **kwargs):
        # Nous récupérons tous les produits dans une variable nommée queryset
        user = self.request.user
        queryset = Issue.objects.filter(author_user_id=user)
        # Vérifions la présence du paramètre ‘issue_id’ dans l’url et si oui alors appliquons notre filtre
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(issue_id=issue_id)

        queryset2 = Issue.objects.all().select_related('project_id')
        project_id = self.kwargs.get("project_pk")
        if project_id is not None:
            queryset = queryset2.filter(project_id=project_id)


        return queryset

    def put_queryset(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = IssueSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_queryset(self, format=None):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_queryset(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self, *args, **kwargs):

        queryset = Comment.objects.all()
        comment_id = self.request.GET.get('comment_id')
        if comment_id is not None:
            queryset = queryset.filter(comment_id=comment_id)


        # queryset2=Comment.objects.filter(issue_id=issue_pk, issue__project=project_pk)
        # issue_id = get_object_or_404(queryset2, id=self.kwargs['issue_pk'])


        queryset2 = Comment.objects.select_related('issue_id')
        project_id = self.kwargs.get("issue__project_pk")
        issue_id = self.kwargs.get("issue_pk")
        if project_id is not None and issue_id is not None:
            queryset = queryset2.filter(issue_id=issue_id, issue__project=project_id)


        # queryset2 = Comment.objects.select_related('issue_id').prefetch_related('comment_id')
        # issue_id = self.kwargs.get("issue_pk")
        # if issue_id is not None:
        #     queryset = queryset2.filter(issue_id=issue_id)


        # Project.objects.filter(project_id=self.kwargs['project_pk'])

        return queryset

    # def retrieve(self, request, pk=None, project_pk=None, issue_pk=None):
    #     queryset = Comment.objects.filter(pk=pk, issue_id=issue_pk, issue__project=project_pk)
    #     issue = get_object_or_404(queryset, pk=pk)
    #     serializer = CommentSerializer(issue)
    #     return Response(serializer.data)

    # def list(self, request, project_pk=None, issue_pk=None):
    #     queryset = Comment.objects.filter(issue_id__project=project_pk, issue_id=issue_pk)
    #     serializer = CommentSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def put_queryset(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CommentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_queryset(self, format=None):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post_queryset(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ContributorViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Contributor.objects.all().select_related('project_id').prefetch_related('user_id')
    serializer_class = ContributorSerializer

    def get_queryset(self, *args, **kwargs):
        project_id = self.kwargs.get("project_pk")
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            print('A project with this id does not exist')
        return self.queryset.filter(project_id=project_id)





