from django.db import models


from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):

    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('pending', 'Pending')
    )

    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    category = models.ManyToManyField(
        Category,
        related_name='posts',
    )
    tags = models.ManyToManyField(Tag, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS, default='draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
    

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

