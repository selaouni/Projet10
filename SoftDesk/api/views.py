from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from api.models import Project, Comment, Issue
# from ..authentication import User
from .serializers import ProjectSerializer, CommentSerializer, IssueSerializer
# from rest_framework import permissions

#
# class UserViewset(ModelViewSet):
#
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         queryset = Usr.objects.all()


class ProjectViewset(ModelViewSet):


    # permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all().select_related('project_id').prefetch_related('author_user_id')
    serializer_class = ProjectSerializer
    def retrieve_byId(self, *args, **kwargs):
        project_id = self.kwargs.get("project_pk")
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            print('A library with this id does not exist')
        return self.queryset.filter(library=project)

        # user_by_projectId = self.request.GET.get('project_id')
        #
        # if user_by_projectId is not None:
        #     queryset = queryset.filter(project_id=user_by_projectId)

        # return queryset

    def get_queryset(self, *args, **kwargs):
        # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Project.objects.all()

        # qs = Album.objects.prefetch_related('tracks')
        # Vérifions la présence du paramètre ‘project_id’ dans l’url et si oui alors appliquons notre filtre

        project_id = self.request.GET.get('project_id')


        # projet = Project.objects.get(id=project_id)
        # queryset = queryset.filter(project_id=project_id)

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

    serializer_class = IssueSerializer

    def get_queryset(self):
        # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Issue.objects.all()
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(project_id=issue_id)
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

    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Comment.objects.all()
        comment_id = self.request.GET.get('comment_id')
        if comment_id is not None:
            queryset = queryset.filter(comment_id=comment_id)
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







# class ProjectAPIView(APIView):
#
#     def get(self, *args, **kwargs):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)





