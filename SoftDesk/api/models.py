from django.db import models




class Users(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=400)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class Projects(models.Model):

    project_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1255)
    type = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE)


class Contributors(models.Model):
    PERMISSION_CHOICES = (
        ('C', 'Create'),
        ('R', 'Read'),
        ('U', 'Update'),
        ('D', 'Delete'),
    )
    user_id = models.IntegerField()
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE) #ForeignKey
    permission = models.CharField(max_length=1, choices=PERMISSION_CHOICES)
    role = models.CharField(max_length=255)





class Issues(models.Model):

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=1255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE) #ForeignKey
    status = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE) #ForeignKey
    assignee_user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE)   #ForeignKey?
    created_time = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):

    comment_id = models.IntegerField()
    description = models.CharField(max_length=1255)
    author_user_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)  # ForeignKey
    created_time = models.DateTimeField(auto_now_add=True)




