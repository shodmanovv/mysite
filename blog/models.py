from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    img = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    likes = models.ManyToManyField(User, through='like', related_name='liked_post', blank=True)
    comments = models.ManyToManyField(User, through='Comment', related_name='commented_post', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} - {self.post.title}"
    
class Like(models.Model):
    post = models.ForeignKey(
        Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} - {self.post.title}"






















