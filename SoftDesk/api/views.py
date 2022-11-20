from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwnerOrReadOnly
from django.db.models import Q


from api.models import Project, Comment, Issue, Contributor
from .serializers import ProjectSerializer, CommentSerializer, IssueSerializer, ContributorSerializer


class ProjectViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer

    def get_queryset(self, *args, **kwargs):
        # Nous récupérons tous les produits dans une variable nommée queryset
        user = self.request.user
        queryset = Project.objects.filter(author_user_id=user.id) | \
                   Project.objects.filter(contributor__user_id=user.id)

        # Vérifions la présence du paramètre ‘project_id’ dans l’url et si oui alors appliquons notre filtre
        project_id = self.request.GET.get('project_id')

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

        user = self.request.user
        queryset2 = Issue.objects.all().filter(author_user_id=user.id).select_related('project_id') | \
                    Issue.objects.filter(project_id__contributor__user_id=user.id) |\
                    Issue.objects.filter(project_id__author_user_id=user.id)
        print(queryset2)
        project_id = self.kwargs.get("project_pk")
        if project_id is not None:
            queryset = queryset2.filter(project_id=project_id)
            # queryset = get_object_or_404(queryset2, id=project_id)

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

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all()
        user = self.request.user
        queryset2 = Comment.objects.all().filter(author_user_id=user.id) | \
                    Comment.objects.filter(issue_id__project_id__contributor__user_id=user.id) | \
                    Comment.objects.filter(issue_id__project_id__author_user_id=user.id)

        project_id = self.kwargs.get('project_pk')
        issue_id = self.kwargs.get('issue_pk')

        if project_id is not None and issue_id is not None:
            queryset = queryset2.filter(issue_id=issue_id) and queryset2.filter(issue_id__project_id=project_id)

        return queryset

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

