from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
