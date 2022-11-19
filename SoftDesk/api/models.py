from django.db import models
from django.conf import settings


class Project(models.Model):
    TYPE_CHOICES = (
        ('BE', 'back-end'),
        ('FE', 'front-end'),
        ('IO', 'iOS'),
        ('AD', 'Android'),
    )
    project_id = models.IntegerField(blank=False, null=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1255, blank=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)


class Contributor(models.Model):
    PERMISSIONS = (
        ('AUTHOR', 'Reader'),
        ('CONTRIBUTOR', 'Editor'),
    )
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, choices=PERMISSIONS)


class Issue(models.Model):
    PRIORITY = (
        ('3 - FAIBLE', 'FAIBLE'),
        ('2 - MOYENNE', 'MOYENNE'),
        ('1 - ÉLEVÉE', 'ÉLEVÉE'),
    )

    PROJECT_STATUT = (
        ('A faire', 'AF'),
        ('En cours', 'EC'),
        ('Terminé', 'OK'),
    )
    BALISE = (
        ('BUG', 'B'),
        ('AMÉLIORATION', 'A'),
        ('TÂCHE', 'T'),
    )
    issue_id = models.IntegerField(blank=False, null=True)
    title = models.CharField(max_length=255, blank=True)
    desc = models.CharField(max_length=1255, blank=True)
    tag = models.CharField(max_length=255,
                           choices=BALISE)  # une balise (BUG, AMÉLIORATION ou TÂCHE)
    priority = models.CharField(max_length=255, choices=PRIORITY)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=PROJECT_STATUT)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       related_name="author_issue")
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                         on_delete=models.CASCADE,
                                         related_name="assigned_issue")  # l’assigné par défaut étant l'auteur lui-même

    created_time = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1255, blank=True)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE, related_name="author_comment")
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
