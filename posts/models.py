from django.db import models
from django.utils import timezone
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=False)
    description = models.CharField(max_length=1000, unique=False)
    pub_date = models.DateTimeField(default=timezone.now())
    liked_by = models.ManyToManyField(User, related_name='liked', blank=True, default=[])

    def get_likes_num(self):
        return self.liked_by.count()
