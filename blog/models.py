from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    DOB = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} - {self.name}"

# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    modified_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title   